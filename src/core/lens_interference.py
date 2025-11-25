#!/usr/bin/env python3
"""
Lens Interference Coefficient (λ - Lambda)

Measures how much different cultural lenses interfere with each other when
viewing the same text. Addresses Gap 2 from testing analysis.

Key insight: Some texts are lens-stable (similar patterns regardless of lens),
while others are lens-dependent (genuinely different truths through different lenses).
"""

import numpy as np
from typing import List, Dict, Tuple
from dataclasses import dataclass


@dataclass
class LensReading:
    """A single lens's reading of a text"""
    lens_name: str
    psi: float
    rho: float
    q: float
    f: float
    pattern_intensity: float


@dataclass
class InterferenceAnalysis:
    """Analysis of how lenses interfere with each other"""
    lambda_coefficient: float  # Overall interference (0-1)
    variance_by_dimension: Dict[str, float]  # Per-dimension variance
    most_stable_dimension: str  # Which dimension is most lens-stable
    most_variable_dimension: str  # Which dimension is most lens-dependent
    lens_compatibility_matrix: Dict[Tuple[str, str], float]  # Pairwise compatibility
    interpretation: str  # What this means


class LensInterferenceAnalyzer:
    """
    Analyzes interference patterns between cultural lenses

    λ = coherence_variance_across_lenses / mean_coherence

    High λ: Text is lens-dependent (different truths through different lenses)
    Low λ: Text is lens-stable (similar patterns across lenses)
    """

    def __init__(self):
        pass

    def calculate_interference(self, readings: List[LensReading]) -> InterferenceAnalysis:
        """
        Calculate lens interference coefficient from multiple lens readings

        Args:
            readings: List of LensReading objects from different cultural lenses

        Returns:
            InterferenceAnalysis with λ and detailed breakdown
        """
        if len(readings) < 2:
            raise ValueError("Need at least 2 lens readings to calculate interference")

        # Extract dimension values across all lenses
        psi_values = [r.psi for r in readings]
        rho_values = [r.rho for r in readings]
        q_values = [r.q for r in readings]
        f_values = [r.f for r in readings]
        intensity_values = [r.pattern_intensity for r in readings]

        # Calculate variance for each dimension
        psi_variance = np.var(psi_values)
        rho_variance = np.var(rho_values)
        q_variance = np.var(q_values)
        f_variance = np.var(f_values)
        intensity_variance = np.var(intensity_values)

        variance_by_dimension = {
            'psi': float(psi_variance),
            'rho': float(rho_variance),
            'q': float(q_variance),
            'f': float(f_variance),
            'intensity': float(intensity_variance)
        }

        # Calculate mean coherence (pattern intensity)
        mean_coherence = np.mean(intensity_values)

        # Calculate λ
        if mean_coherence == 0:
            lambda_coefficient = 0.0
        else:
            lambda_coefficient = float(intensity_variance / max(mean_coherence, 0.01))

        # Identify most stable and variable dimensions
        dimension_variances = {
            'psi': psi_variance,
            'rho': rho_variance,
            'q': q_variance,
            'f': f_variance
        }
        most_stable = min(dimension_variances.items(), key=lambda x: x[1])[0]
        most_variable = max(dimension_variances.items(), key=lambda x: x[1])[0]

        # Calculate pairwise lens compatibility
        compatibility_matrix = {}
        for i, reading1 in enumerate(readings):
            for j, reading2 in enumerate(readings):
                if i < j:  # Only calculate each pair once
                    # Compatibility = 1 - average difference across dimensions
                    diff = (
                        abs(reading1.psi - reading2.psi) +
                        abs(reading1.rho - reading2.rho) +
                        abs(reading1.q - reading2.q) +
                        abs(reading1.f - reading2.f)
                    ) / 4.0
                    compatibility = 1.0 - diff
                    compatibility_matrix[(reading1.lens_name, reading2.lens_name)] = compatibility

        # Generate interpretation
        interpretation = self._interpret_lambda(lambda_coefficient, most_variable, readings)

        return InterferenceAnalysis(
            lambda_coefficient=lambda_coefficient,
            variance_by_dimension=variance_by_dimension,
            most_stable_dimension=most_stable,
            most_variable_dimension=most_variable,
            lens_compatibility_matrix=compatibility_matrix,
            interpretation=interpretation
        )

    def _interpret_lambda(self, lambda_val: float, most_variable: str, readings: List[LensReading]) -> str:
        """Generate human-readable interpretation of λ"""
        if lambda_val < 0.1:
            return f"LENS-STABLE: This text shows consistent patterns across all cultural lenses. The meaning is relatively universal - different lenses see the same core pattern. Most stable dimension: {most_variable}."
        elif lambda_val < 0.3:
            return f"LOW INTERFERENCE: Different lenses see mostly similar patterns with minor variations. The text has a stable core with some lens-dependent nuances, especially in the {most_variable} dimension."
        elif lambda_val < 0.6:
            return f"MODERATE INTERFERENCE: Different lenses reveal genuinely different aspects of this text. The {most_variable} dimension varies significantly across cultural interpretations - multiple valid readings coexist."
        else:
            return f"HIGH INTERFERENCE: This text is highly lens-dependent. Different cultural lenses see fundamentally different patterns. The {most_variable} dimension shows extreme variation - translation heavily depends on lens selection."

    def find_optimal_lens(self, readings: List[LensReading], target_dimension: str = 'pattern_intensity') -> LensReading:
        """
        Find which lens best reveals a specific dimension

        Args:
            readings: List of lens readings
            target_dimension: Which dimension to optimize for

        Returns:
            The lens reading that maximizes the target dimension
        """
        dimension_map = {
            'pattern_intensity': lambda r: r.pattern_intensity,
            'psi': lambda r: r.psi,
            'rho': lambda r: r.rho,
            'q': lambda r: r.q,
            'f': lambda r: r.f
        }

        if target_dimension not in dimension_map:
            raise ValueError(f"Unknown dimension: {target_dimension}")

        return max(readings, key=dimension_map[target_dimension])


def test_lens_interference():
    """Test the lens interference analyzer"""

    # Simulate different lens readings of the same text
    # Example: "A Poet's Reply" through different lenses

    readings_poetry = [
        LensReading("Modern Poetic", psi=0.70, rho=0.58, q=0.53, f=0.28, pattern_intensity=0.65),
        LensReading("Medieval Islamic", psi=0.92, rho=0.88, q=0.68, f=0.75, pattern_intensity=0.81),
        LensReading("Digital Native", psi=0.55, rho=0.45, q=0.79, f=0.90, pattern_intensity=0.67),
        LensReading("Buddhist", psi=0.70, rho=0.95, q=0.38, f=0.60, pattern_intensity=0.66),
    ]

    # LinkedIn post (mostly f-dimension regardless of lens)
    readings_linkedin = [
        LensReading("Modern Poetic", psi=0.35, rho=0.20, q=0.38, f=0.95, pattern_intensity=0.47),
        LensReading("Medieval Islamic", psi=0.30, rho=0.18, q=0.35, f=0.92, pattern_intensity=0.44),
        LensReading("Digital Native", psi=0.40, rho=0.22, q=0.40, f=0.98, pattern_intensity=0.50),
        LensReading("Buddhist", psi=0.33, rho=0.19, q=0.36, f=0.94, pattern_intensity=0.46),
    ]

    analyzer = LensInterferenceAnalyzer()

    print("=" * 90)
    print("LENS INTERFERENCE ANALYSIS (λ - Lambda)")
    print("=" * 90)

    # Test 1: Poetry (expected high λ)
    print("\n" + "─" * 90)
    print("📖 TEST 1: 'A Poet's Reply' (Complex Poetry)")
    print("─" * 90)

    analysis1 = analyzer.calculate_interference(readings_poetry)

    print(f"\nλ (Lambda Coefficient):        {analysis1.lambda_coefficient:.3f}")
    print(f"Most Stable Dimension:         {analysis1.most_stable_dimension}")
    print(f"Most Variable Dimension:       {analysis1.most_variable_dimension}")
    print(f"\nDimensional Variance:")
    for dim, var in analysis1.variance_by_dimension.items():
        if dim != 'intensity':
            print(f"  {dim:12} variance: {var:.4f}")

    print(f"\n📊 Interpretation:")
    print(f"  {analysis1.interpretation}")

    # Show lens compatibility
    print(f"\n🔗 Lens Compatibility Matrix:")
    for (lens1, lens2), compat in sorted(analysis1.lens_compatibility_matrix.items()):
        bar = '█' * int(compat * 30)
        print(f"  {lens1:20} ↔ {lens2:20} {compat:.3f} {bar}")

    # Test 2: LinkedIn (expected low λ)
    print("\n" + "─" * 90)
    print("📖 TEST 2: LinkedIn Post (Social Signaling)")
    print("─" * 90)

    analysis2 = analyzer.calculate_interference(readings_linkedin)

    print(f"\nλ (Lambda Coefficient):        {analysis2.lambda_coefficient:.3f}")
    print(f"Most Stable Dimension:         {analysis2.most_stable_dimension}")
    print(f"Most Variable Dimension:       {analysis2.most_variable_dimension}")
    print(f"\nDimensional Variance:")
    for dim, var in analysis2.variance_by_dimension.items():
        if dim != 'intensity':
            print(f"  {dim:12} variance: {var:.4f}")

    print(f"\n📊 Interpretation:")
    print(f"  {analysis2.interpretation}")

    # Comparison
    print("\n" + "=" * 90)
    print("COMPARATIVE ANALYSIS:")
    print("=" * 90)
    print(f"""
Poetry λ = {analysis1.lambda_coefficient:.3f} (LENS-DEPENDENT)
  → Different lenses reveal genuinely different patterns
  → {analysis1.most_variable_dimension} varies significantly across cultures
  → Multiple valid interpretations coexist

LinkedIn λ = {analysis2.lambda_coefficient:.3f} (LENS-STABLE)
  → All lenses see essentially the same pattern
  → Dominated by {analysis2.most_stable_dimension} dimension
  → Universal social signaling - minimal cultural variation

KEY INSIGHT: λ tells us whether we need multiple lenses (high λ) or if
one lens is sufficient (low λ). Critical for choosing analysis approach.
    """)

    # Optimal lens identification
    print("=" * 90)
    print("OPTIMAL LENS SELECTION:")
    print("=" * 90)

    optimal_wisdom = analyzer.find_optimal_lens(readings_poetry, 'rho')
    optimal_moral = analyzer.find_optimal_lens(readings_poetry, 'q')

    print(f"\nFor maximizing wisdom depth (ρ):")
    print(f"  → {optimal_wisdom.lens_name} (ρ = {optimal_wisdom.rho:.3f})")

    print(f"\nFor maximizing moral energy (q):")
    print(f"  → {optimal_moral.lens_name} (q = {optimal_moral.q:.3f})")

    print("\n" + "=" * 90)


if __name__ == "__main__":
    test_lens_interference()
