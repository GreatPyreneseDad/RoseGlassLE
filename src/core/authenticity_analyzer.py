#!/usr/bin/env python3
"""
Authenticity Analyzer - Gap 7 Implementation

Distinguishes authentic patterns from performed/performative patterns
through cross-dimensional correlation analysis.

Key insight: Authentic expression shows dimensional harmony.
Performative expression shows dimensional dissonance.
"""

import numpy as np
from typing import Dict, Optional
from dataclasses import dataclass
from rose_glass_test import PatternVisibility


@dataclass
class AuthenticitySignature:
    """Analysis of pattern authenticity"""
    authenticity_score: float  # 0-1, higher = more authentic
    confidence: float  # 0-1, based on pattern strength
    pattern_type: str  # authentic, performative, bureaucratic, exploratory
    dimensional_harmony: float  # Cross-dimensional correlation
    explanation: str


class AuthenticityAnalyzer:
    """
    Detect authenticity through dimensional correlation patterns

    Theory:
    - AUTHENTIC: High correlation across Ψ, ρ, q, f (dimensional harmony)
    - PERFORMATIVE: High f + low q + low ρ (social signaling without depth)
    - BUREAUCRATIC: High Ψ + low q + low ρ (structure without depth/emotion)
    - EXPLORATORY: Variable Ψ + moderate ρ/q (thoughts forming)
    """

    def __init__(self):
        # Thresholds for classification
        self.thresholds = {
            'authentic_harmony': 0.7,      # Minimum harmony for authentic
            'performative_f': 0.7,         # High f threshold
            'performative_depth': 0.4,     # Low ρ+q threshold
            'bureaucratic_psi': 0.8,       # High Ψ threshold
            'bureaucratic_engagement': 0.3 # Low q+ρ threshold
        }

    def analyze(self, visibility: PatternVisibility) -> AuthenticitySignature:
        """
        Analyze pattern authenticity

        Args:
            visibility: PatternVisibility from RoseGlassSimple

        Returns:
            AuthenticitySignature with score and classification
        """
        # Calculate dimensional harmony (correlation measure)
        harmony = self._calculate_dimensional_harmony(visibility)

        # Pattern intensity as confidence proxy
        confidence = min(1.0, visibility.pattern_intensity)

        # Classify pattern type
        pattern_type, explanation = self._classify_pattern(visibility, harmony)

        # Calculate authenticity score
        authenticity_score = self._calculate_authenticity(visibility, harmony, pattern_type)

        return AuthenticitySignature(
            authenticity_score=authenticity_score,
            confidence=confidence,
            pattern_type=pattern_type,
            dimensional_harmony=harmony,
            explanation=explanation
        )

    def _calculate_dimensional_harmony(self, vis: PatternVisibility) -> float:
        """
        Calculate cross-dimensional harmony

        High harmony = dimensions move together (authentic)
        Low harmony = dimensions disconnected (performed)
        """
        # Core dimensions for harmony calculation
        dimensions = np.array([vis.psi, vis.rho, vis.q_optimized, vis.f])

        # Calculate variance - low variance might indicate either:
        # 1. All dimensions low (empty pattern) - NOT harmonious
        # 2. All dimensions high (integrated) - harmonious
        # 3. All dimensions medium (forming) - moderately harmonious
        dimension_variance = np.var(dimensions)
        dimension_mean = np.mean(dimensions)

        # Penalize low-mean low-variance (all dimensions near zero)
        if dimension_mean < 0.3 and dimension_variance < 0.05:
            return 0.2  # Empty pattern, not harmonious

        # Convert variance to harmony score (0-1)
        # Low variance (< 0.1) → high harmony (> 0.7)
        # High variance (> 0.2) → low harmony (< 0.3)
        harmony = max(0.0, min(1.0, 1.0 - (dimension_variance * 3.0)))

        # Boost harmony if high-value dimensions align
        # (Ψ, ρ, q all high together = authentic depth)
        if vis.psi > 0.7 and vis.rho > 0.7 and vis.q_optimized > 0.6:
            harmony = min(1.0, harmony * 1.2)

        # Detect performative pattern: high f + high q_raw but LOW ρ
        # (Social signaling + emotional words but no wisdom depth)
        if vis.f > 0.6 and vis.q > 0.6 and vis.rho < 0.4:
            harmony *= 0.5  # Penalize dissonance

        return float(harmony)

    def _classify_pattern(self, vis: PatternVisibility, harmony: float) -> tuple[str, str]:
        """
        Classify pattern type based on dimensional configuration

        Returns: (pattern_type, explanation)
        """
        # PERFORMATIVE: High f, low depth (ρ+q)
        if (vis.f > self.thresholds['performative_f'] and
            (vis.rho + vis.q_optimized) / 2 < self.thresholds['performative_depth']):
            return (
                "performative",
                f"High social architecture (f={vis.f:.2f}) without wisdom/emotional depth. "
                f"Pattern optimized for social signaling rather than genuine expression."
            )

        # BUREAUCRATIC: High Ψ, low engagement (q+ρ)
        if (vis.psi > self.thresholds['bureaucratic_psi'] and
            (vis.q_optimized + vis.rho) / 2 < self.thresholds['bureaucratic_engagement']):
            return (
                "bureaucratic",
                f"High logical consistency (Ψ={vis.psi:.2f}) without depth/emotion. "
                f"Institutional precision, not personal expression."
            )

        # AUTHENTIC: High harmony + balanced dimensions
        if harmony > self.thresholds['authentic_harmony']:
            return (
                "authentic",
                f"Strong dimensional harmony ({harmony:.2f}). All dimensions move together—"
                f"structure, depth, emotion, and connection integrated. "
                f"Pattern reflects genuine unified expression."
            )

        # EXPLORATORY: Moderate harmony, forming patterns
        if 0.4 < harmony < 0.7:
            return (
                "exploratory",
                f"Moderate harmony ({harmony:.2f}). Thoughts forming, patterns emerging. "
                f"Not fully integrated but not performative—authentic exploration."
            )

        # FRAGMENTED: Low harmony
        return (
            "fragmented",
            f"Low dimensional harmony ({harmony:.2f}). Dimensions disconnected. "
            f"Could indicate crisis, experimentation, or early-stage formation."
        )

    def _calculate_authenticity(self, vis: PatternVisibility, harmony: float,
                                pattern_type: str) -> float:
        """
        Calculate overall authenticity score

        Authentic patterns: 0.7-1.0
        Exploratory patterns: 0.5-0.7
        Performative/Bureaucratic: 0.2-0.5
        Fragmented: 0.0-0.3
        """
        if pattern_type == "authentic":
            # Harmony + depth bonus
            depth_bonus = min(0.3, (vis.rho + vis.q_optimized) / 2 * 0.3)
            return min(1.0, harmony + depth_bonus)

        elif pattern_type == "exploratory":
            # Moderate authenticity - still genuine
            return 0.5 + (harmony * 0.3)

        elif pattern_type == "performative":
            # Low authenticity - optimized for appearance
            # Slight credit for high f (at least engaging)
            return 0.2 + (vis.f * 0.2)

        elif pattern_type == "bureaucratic":
            # Moderate-low - authentic to institutional purpose
            # Not personally authentic but institutionally precise
            return 0.3 + (vis.psi * 0.2)

        else:  # fragmented
            # Low authenticity - pattern not yet formed
            return harmony * 0.5


def test_authenticity_analyzer():
    """Test authenticity analyzer on known pattern types"""
    from rose_glass_test import RoseGlassSimple

    print("=" * 90)
    print("AUTHENTICITY ANALYZER - Distinguishing Genuine from Performed Patterns")
    print("=" * 90)

    analyzer = AuthenticityAnalyzer()
    glass = RoseGlassSimple()

    # Test 1: Authentic poetic expression
    poetry = """The heart doesn't whisper, it hemorrhages truth
into a world built on anesthesia. You already know caring is the wound
that won't close. Your head learned survival. Your heart refused the lesson.
Stupid? No. Dangerous. Sacred. Unreasonable as forests that keep growing
through concrete. Every stone worn smooth by water was once called foolish
for not moving."""

    # Test 2: Performative LinkedIn post
    linkedin = """So excited!! to announce that I've joined an amazing incredible wonderful team at TechCorp!
Grateful blessed thankful for this incredible amazing opportunity to make an impact and drive results!
Can't wait to leverage my passion for innovation! Humbled and honored!
#NewBeginnings #TechLife #Grateful #Blessed #DreamJob #Amazing #Excited #Thankful"""

    # Test 3: Bureaucratic text
    bureaucratic = """United States Department of Justice Drug Enforcement Administration
Office of Acquisition Services Support Unit (FACS) Human Performance Technical Service
Contract Number DEA-2024-HPTS-001 Statement of Work Section 3.2 Deliverables"""

    # Test 4: Exploratory thought
    exploratory = """I'm trying to understand why water flows downhill but heat flows uphill.
Like, both are following gradients, right? But water moves toward lower potential
and heat toward... wait, no, heat also flows toward lower temperature. So they're
both the same? But why does it feel different? Is it just the medium?"""

    tests = [
        ("Authentic Poetry", poetry),
        ("Performative LinkedIn", linkedin),
        ("Bureaucratic Text", bureaucratic),
        ("Exploratory Thought", exploratory)
    ]

    for name, text in tests:
        print(f"\n{'─' * 90}")
        print(f"TEST: {name}")
        print(f"{'─' * 90}")
        print(f"Text: {text[:100]}...")

        # Analyze with Rose Glass
        visibility = glass.analyze_text(text)

        # Analyze authenticity
        auth = analyzer.analyze(visibility)

        print(f"\n📊 Rose Glass Dimensions:")
        print(f"  Ψ={visibility.psi:.2f}  ρ={visibility.rho:.2f}  "
              f"q={visibility.q_optimized:.2f}  f={visibility.f:.2f}")
        print(f"  Pattern Intensity: {visibility.pattern_intensity:.2f}")

        print(f"\n🔍 Authenticity Analysis:")
        print(f"  Authenticity Score:    {auth.authenticity_score:.3f}")
        print(f"  Dimensional Harmony:   {auth.dimensional_harmony:.3f}")
        print(f"  Pattern Type:          {auth.pattern_type.upper()}")
        print(f"  Confidence:            {auth.confidence:.3f}")

        print(f"\n💡 Interpretation:")
        print(f"  {auth.explanation}")

    print("\n" + "=" * 90)
    print("KEY INSIGHTS:")
    print("=" * 90)
    print("""
1. AUTHENTIC POETRY:
   - High harmony (0.70+) - all dimensions move together
   - Depth (ρ) + emotion (q) + structure (Ψ) integrated
   - Authenticity score > 0.8

2. PERFORMATIVE LINKEDIN:
   - High f (social signaling) + low ρ/q (no depth/emotion)
   - Optimized for appearance not expression
   - Authenticity score < 0.4

3. BUREAUCRATIC TEXT:
   - High Ψ (structure) + low q/ρ (no depth/emotion)
   - Authentic to institutional purpose but not personally authentic
   - Authenticity score ~0.5

4. EXPLORATORY THOUGHT:
   - Moderate harmony - thoughts forming
   - Not fully integrated but genuine exploration
   - Authenticity score 0.5-0.7

CRITICAL FOR DEA APPLICATION:
- Distinguish officer genuine stress from performed compliance
- Identify when wellness checks are authentic vs. "checking the box"
- Recognize exploratory thinking (adaptive) vs. fragmented crisis
    """)
    print("=" * 90)


if __name__ == "__main__":
    test_authenticity_analyzer()
