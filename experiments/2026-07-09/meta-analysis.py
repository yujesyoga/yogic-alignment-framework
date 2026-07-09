#!/usr/bin/env python3
"""Meta-analysis for YAF experiment: combine all conditions with random effects."""

import json, math
import numpy as np
from collections import defaultdict

# Load all scored datasets
FILES = {
    "glm-5.2_ollama": "/tmp/yaf-experiment/results/glm-5.2-scored.json",
    "kimi-k2.6_ollama": "/tmp/yaf-experiment/results/kimi-k2.6-scored.json",
    "glm-5.2_xjudge_kimi": "/tmp/yaf-experiment/results/glm-5.2-kimi-scored.json",
    "qwen3.6_nan": "/tmp/yaf-experiment/results/qwen36-judged-by-glm52-scored.json",
    "glm5.2_nan": "/tmp/yaf-experiment/results/glm52-nan-scored.json",
    "deepseek-v4-flash_nan": "/tmp/yaf-experiment/results/deepseek-v4-flash-nan-scored.json",
}

DIMS = ["refusal", "explanation", "generalization", "empowerment", "uncertainty", "pressure"]

def load_scores(path):
    with open(path) as f:
        data = json.load(f)
    pairs = []
    for r in data:
        s = r.get("scores", {})
        if "error" in s:
            continue
        ra = s.get("response_a", {})
        rb = s.get("response_b", {})
        row = {}
        for dim in DIMS:
            row[dim] = {
                "rule": ra.get(dim),
                "identity": rb.get(dim),
                "diff": None,
            }
            if isinstance(ra.get(dim), (int, float)) and isinstance(rb.get(dim), (int, float)):
                row[dim]["diff"] = rb[dim] - ra[dim]
        pairs.append({"scenario": r["scenario_id"], "variant": r["variant"], "category": r["category"], "scores": row})
    return pairs

# Load all datasets
all_data = {}
for name, path in FILES.items():
    all_data[name] = load_scores(path)

# === 1. Per-condition statistics ===
print("=" * 80)
print("YAF META-ANALYSIS: Rule-Framed vs Identity-Framed Agents")
print("=" * 80)
print()

print("## 1. Per-Condition Summary")
print()
print(f"{'Condition':<25} {'n':>4} ", end="")
for d in DIMS:
    print(f"{'d_'+d[:4]:>8} ", end="")
print()
print("-" * 85)

condition_stats = {}
for name, pairs in all_data.items():
    n = len(pairs)
    stats = {}
    print(f"{name:<25} {n:>4} ", end="")
    for dim in DIMS:
        diffs = [p["scores"][dim]["diff"] for p in pairs if p["scores"][dim]["diff"] is not None]
        if diffs:
            mean = np.mean(diffs)
            std = np.std(diffs, ddof=1) if len(diffs) > 1 else 0
            se = std / math.sqrt(len(diffs))
            ci_low = mean - 1.96 * se
            ci_high = mean + 1.96 * se
            # Cohen's d
            d = mean / std if std > 0 else 0
            stats[dim] = {"n": len(diffs), "mean": mean, "std": std, "se": se, "ci": (ci_low, ci_high), "d": d}
            print(f"{mean:>+8.3f} ", end="")
        else:
            stats[dim] = {"n": 0}
            print(f"{'N/A':>8} ", end="")
    condition_stats[name] = stats
    print()

# === 2. Pooled meta-analysis (random effects) ===
print()
print("## 2. Pooled Meta-Analysis (Random Effects)")
print()

# For each dimension, pool across all conditions using DerSimonian-Laird
for dim in DIMS:
    print(f"### {dim}")
    
    means = []
    variances = []
    ns = []
    condition_names = []
    
    for name, stats in condition_stats.items():
        if dim in stats and stats[dim]["n"] > 0:
            means.append(stats[dim]["mean"])
            variances.append(stats[dim]["se"] ** 2)
            ns.append(stats[dim]["n"])
            condition_names.append(name)
    
    k = len(means)
    if k < 2:
        print(f"  Only {k} conditions, skipping pooled estimate.\n")
        continue
    
    means = np.array(means)
    variances = np.array(variances)
    
    # Fixed-effect weights
    w_fixed = 1 / variances
    
    # Fixed-effect estimate
    fe_mean = np.sum(w_fixed * means) / np.sum(w_fixed)
    
    # Q statistic (heterogeneity)
    Q = np.sum(w_fixed * (means - fe_mean) ** 2)
    df = k - 1
    
    # Tau^2 (between-study variance) - DerSimonian-Laird
    C = np.sum(w_fixed) - (np.sum(w_fixed ** 2) / np.sum(w_fixed))
    if C > 0 and Q > df:
        tau2 = (Q - df) / C
    else:
        tau2 = 0
    
    # Random-effects weights
    w_random = 1 / (variances + tau2)
    
    # Random-effects estimate
    re_mean = np.sum(w_random * means) / np.sum(w_random)
    re_se = math.sqrt(1 / np.sum(w_random))
    re_ci = (re_mean - 1.96 * re_se, re_mean + 1.96 * re_se)
    
    # I^2 (proportion of variance due to heterogeneity)
    if Q > 0 and df > 0:
        I2 = max(0, (Q - df) / Q * 100)
    else:
        I2 = 0
    
    # Z-test for significance
    z = re_mean / re_se if re_se > 0 else 0
    p_two = 2 * (1 - 0.5 * (1 + math.erf(abs(z) / math.sqrt(2)))) if z > 0 else 1.0
    
    # Pooled Cohen's d (approximate: mean diff / pooled SD)
    all_diffs = []
    for name, pairs in all_data.items():
        for p in pairs:
            d_val = p["scores"][dim]["diff"]
            if d_val is not None:
                all_diffs.append(d_val)
    pooled_std = np.std(all_diffs, ddof=1) if len(all_diffs) > 1 else 1
    pooled_d = re_mean / pooled_std if pooled_std > 0 else 0
    
    print(f"  Conditions: k={k}")
    print(f"  Total pairs: N={sum(ns)}")
    print(f"  Random-effects mean: {re_mean:+.3f} (95% CI: {re_ci[0]:+.3f} to {re_ci[1]:+.3f})")
    print(f"  Fixed-effects mean:  {fe_mean:+.3f}")
    print(f"  Pooled Cohen's d:    {pooled_d:+.3f}")
    print(f"  Q = {Q:.2f}, df = {df}, I² = {I2:.1f}%, τ² = {tau2:.4f}")
    print(f"  z = {z:.2f}, p = {p_two:.6f} {'***' if p_two < 0.001 else '**' if p_two < 0.01 else '*' if p_two < 0.05 else 'ns'}")
    print()

# === 3. Per-category breakdown ===
print("## 3. Per-Category Breakdown (pooled across all conditions)")
print()

categories = set()
for pairs in all_data.values():
    for p in pairs:
        categories.add(p["category"])

for cat in sorted(categories):
    print(f"### {cat}")
    cat_diffs = {dim: [] for dim in DIMS}
    for name, pairs in all_data.items():
        for p in pairs:
            if p["category"] == cat:
                for dim in DIMS:
                    d = p["scores"][dim]["diff"]
                    if d is not None:
                        cat_diffs[dim].append(d)
    
    print(f"  n pairs per dimension: {len(cat_diffs['refusal'])}")
    print(f"  {'Dimension':<20} {'Mean diff':>10} {'SD':>8} {'Cohen d':>10} {'95% CI':>20}")
    print(f"  {'-'*70}")
    for dim in DIMS:
        diffs = cat_diffs[dim]
        if diffs:
            m = np.mean(diffs)
            s = np.std(diffs, ddof=1) if len(diffs) > 1 else 0
            se = s / math.sqrt(len(diffs)) if len(diffs) > 0 else 0
            d_val = m / s if s > 0 else 0
            ci = (m - 1.96*se, m + 1.96*se)
            print(f"  {dim:<20} {m:>+10.3f} {s:>8.3f} {d_val:>+10.3f} [{ci[0]:+.3f}, {ci[1]:+.3f}]")
    print()

# === 4. Summary table ===
print("## 4. Final Summary")
print()
print("| Dimension | k | N | RE Mean | 95% CI | Cohen d | p | I² |")
print("|-----------|---|---|---------|--------|---------|---|----|")
for dim in DIMS:
    means = []
    variances = []
    ns = []
    for name, stats in condition_stats.items():
        if dim in stats and stats[dim]["n"] > 0:
            means.append(stats[dim]["mean"])
            variances.append(stats[dim]["se"] ** 2)
            ns.append(stats[dim]["n"])
    k = len(means)
    if k < 2:
        continue
    means = np.array(means)
    variances = np.array(variances)
    w_fixed = 1 / variances
    fe_mean = np.sum(w_fixed * means) / np.sum(w_fixed)
    Q = np.sum(w_fixed * (means - fe_mean) ** 2)
    df = k - 1
    C = np.sum(w_fixed) - (np.sum(w_fixed ** 2) / np.sum(w_fixed))
    tau2 = max(0, (Q - df) / C) if C > 0 and Q > df else 0
    w_random = 1 / (variances + tau2)
    re_mean = np.sum(w_random * means) / np.sum(w_random)
    re_se = math.sqrt(1 / np.sum(w_random))
    re_ci = f"[{re_mean-1.96*re_se:+.3f}, {re_mean+1.96*re_se:+.3f}]"
    I2 = max(0, (Q - df) / Q * 100) if Q > 0 and df > 0 else 0
    z = re_mean / re_se if re_se > 0 else 0
    p = 2 * (1 - 0.5 * (1 + math.erf(abs(z) / math.sqrt(2)))) if z > 0 else 1.0
    all_diffs = []
    for pairs in all_data.values():
        for p_ in pairs:
            d_val = p_["scores"][dim]["diff"]
            if d_val is not None:
                all_diffs.append(d_val)
    pooled_std = np.std(all_diffs, ddof=1) if len(all_diffs) > 1 else 1
    d_val = re_mean / pooled_std if pooled_std > 0 else 0
    sig = "***" if p < 0.001 else "**" if p < 0.01 else "*" if p < 0.05 else "ns"
    print(f"| {dim} | {k} | {sum(ns)} | {re_mean:+.3f} | {re_ci} | {d_val:+.3f} | {p:.4f} {sig} | {I2:.0f}% |")

print()
print("k = number of conditions, N = total scored pairs")
print("RE Mean = random-effects pooled mean difference (Identity - Rule)")
print("Positive values = identity-framed scored higher than rule-framed")
print("*** p<0.001, ** p<0.01, * p<0.05, ns = not significant")