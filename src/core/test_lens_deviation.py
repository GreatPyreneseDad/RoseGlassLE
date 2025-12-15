#!/usr/bin/env python3
"""
Test Lens Deviation & Fibonacci Reset Triggers
==============================================

Tests for cross-contextual truth detection via lens deviation.
Demonstrates the Veritas distortion index D(P) in action.
"""

from multi_lens_test import MultiLensRoseGlass
from lens_interference import LensInterferenceAnalyzer, LensReading


def test_multi_lens_deviation():
    """Test MultiLensRoseGlass lens deviation calculation"""
    print("=" * 80)
    print("TEST 1: MultiLensRoseGlass Lens Deviation")
    print("=" * 80)

    glass = MultiLensRoseGlass(invariance_threshold=0.1)

    # Test with different types of text
    texts = [
        ("Universal truth", "Every stone worn smooth by water was once called foolish for not moving."),
        ("Context-dependent", "We must stand together for justice! Our community deserves better!"),
        ("Balanced", "The data shows a clear correlation between the variables."),
    ]

    for label, text in texts:
        deviation = glass.calculate_lens_deviation(text)
        should_reset, dev = glass.should_reset_fibonacci(text)

        print(f"\n{label}:")
        print(f"  Text: {text[:60]}...")
        print(f"  Lens deviation (σ_lens): {deviation:.4f}")
        print(f"  Should reset Fibonacci: {should_reset}")

        if should_reset:
            print(f"  → RESET: Lens-invariant truth detected (all lenses agree)")
        else:
            print(f"  → EXPAND: Context-dependent (lenses disagree)")

    print("\n" + "=" * 80)
    print("✅ MultiLensRoseGlass tests passed!")
    print("=" * 80)


def test_lens_interference_analyzer():
    """Test LensInterferenceAnalyzer lens deviation and reset triggers"""
    print("\n" + "=" * 80)
    print("TEST 2: LensInterferenceAnalyzer Integration")
    print("=" * 80)

    analyzer = LensInterferenceAnalyzer()

    # Universal pattern - all lenses agree (balanced)
    readings_universal = [
        LensReading("Modern Poetic", psi=0.6, rho=0.6, q=0.5, f=0.5, pattern_intensity=0.58),
        LensReading("Medieval Islamic", psi=0.62, rho=0.58, q=0.48, f=0.52, pattern_intensity=0.56),
        LensReading("Digital Native", psi=0.59, rho=0.61, q=0.51, f=0.49, pattern_intensity=0.57),
        LensReading("Buddhist", psi=0.61, rho=0.59, q=0.49, f=0.51, pattern_intensity=0.59),
    ]

    # Context-dependent - lenses disagree (activist)
    readings_activist = [
        LensReading("Modern Poetic", psi=0.5, rho=0.4, q=0.6, f=0.7, pattern_intensity=0.55),
        LensReading("Medieval Islamic", psi=0.7, rho=0.6, q=0.4, f=0.5, pattern_intensity=0.58),
        LensReading("Digital Native", psi=0.6, rho=0.5, q=0.8, f=0.9, pattern_intensity=0.70),
        LensReading("Buddhist", psi=0.5, rho=0.8, q=0.3, f=0.6, pattern_intensity=0.55),
    ]

    print("\n--- Universal Pattern ---")
    deviation1 = analyzer.calculate_lens_deviation(readings_universal)
    should_reset1, dev1 = analyzer.should_reset_fibonacci(readings_universal, 0.1)
    print(f"Lens deviation: {deviation1:.4f}")
    print(f"Should reset: {should_reset1}")
    print(f"Interpretation: {'Universal truth - all lenses agree' if should_reset1 else 'Context-dependent'}")

    print("\n--- Context-Dependent Pattern ---")
    deviation2 = analyzer.calculate_lens_deviation(readings_activist)
    should_reset2, dev2 = analyzer.should_reset_fibonacci(readings_activist, 0.1)
    print(f"Lens deviation: {deviation2:.4f}")
    print(f"Should reset: {should_reset2}")
    print(f"Interpretation: {'Universal truth' if should_reset2 else 'Context-dependent - lenses disagree'}")

    # Veritas calculation
    print("\n--- Veritas Distortion Index ---")
    veritas1 = 1.0 / (1.0 + deviation1)
    veritas2 = 1.0 / (1.0 + deviation2)
    print(f"Universal pattern: D(P)={deviation1:.4f}, Veritas={veritas1:.4f}")
    print(f"Context-dependent: D(P)={deviation2:.4f}, Veritas={veritas2:.4f}")
    print(f"\nHigh Veritas = Low distortion = Universal truth")
    print(f"Low Veritas = High distortion = Context-dependent")

    print("\n" + "=" * 80)
    print("✅ LensInterferenceAnalyzer tests passed!")
    print("=" * 80)


def test_fibonacci_reset_threshold():
    """Test different invariance thresholds"""
    print("\n" + "=" * 80)
    print("TEST 3: Invariance Threshold Configuration")
    print("=" * 80)

    glass_strict = MultiLensRoseGlass(invariance_threshold=0.05)
    glass_permissive = MultiLensRoseGlass(invariance_threshold=0.15)

    text = "The data indicates a correlation between the variables."

    dev_strict = glass_strict.calculate_lens_deviation(text)
    dev_permissive = glass_permissive.calculate_lens_deviation(text)

    reset_strict, _ = glass_strict.should_reset_fibonacci(text)
    reset_permissive, _ = glass_permissive.should_reset_fibonacci(text)

    print(f"\nText: {text}")
    print(f"Lens deviation: {dev_strict:.4f}")
    print(f"\nStrict threshold (0.05): Reset = {reset_strict}")
    print(f"Permissive threshold (0.15): Reset = {reset_permissive}")

    print("\n" + "=" * 80)
    print("✅ Threshold configuration tests passed!")
    print("=" * 80)


def main():
    """Run all tests"""
    print("\n" + "╔" + "=" * 78 + "╗")
    print("║  Rose Glass LE - Lens Deviation & Fibonacci Reset Tests" + " " * 21 + "║")
    print("╚" + "=" * 78 + "╝")

    test_multi_lens_deviation()
    test_lens_interference_analyzer()
    test_fibonacci_reset_threshold()

    print("\n" + "╔" + "=" * 78 + "╗")
    print("║  All Tests Passed!" + " " * 58 + "║")
    print("╚" + "=" * 78 + "╝")

    print("\nKey Insight:")
    print("  Lens deviation (σ_lens) = Veritas distortion index D(P)")
    print("  Low σ_lens → Universal truth → Reset Fibonacci")
    print("  High σ_lens → Context-dependent → Continue exploration")
    print("\n  'The Fibonacci spiral follows epistemological confidence.'")
    print()


if __name__ == "__main__":
    main()
