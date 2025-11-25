#!/usr/bin/env python3
"""
Neurodivergent Communication Calibrations

Critical for DEA Human Performance application. Law enforcement populations
include significant neurodivergent representation (autism, ADHD, etc.).

Key insight: Neurodivergent communication patterns have different saturation
curves, activation thresholds, and dimensional coupling than neurotypical patterns.
"""

from dataclasses import dataclass
from typing import Dict, List, Optional
from enum import Enum


class NeurodivergenceType(Enum):
    """Types of neurodivergent communication patterns"""
    AUTISM_SPECTRUM = "autism_spectrum"
    ADHD = "adhd"
    DYSLEXIA = "dyslexia"
    HIGH_STRESS_TRAUMA = "high_stress_trauma"  # For law enforcement/veteran contexts
    GENERAL = "general"  # Parent class for all neurodivergent patterns


@dataclass
class CulturalCalibration:
    """Base cultural calibration (from original Rose Glass)"""
    name: str
    description: str
    km: float = 0.3  # Saturation curve midpoint
    ki: float = 2.0  # Inhibition threshold
    coupling_strength: float = 0.15  # Cross-dimensional coupling
    expected_patterns: Dict[str, str] = None
    breathing_pattern: str = "standard"

    def __post_init__(self):
        if self.expected_patterns is None:
            self.expected_patterns = {}


class NeurodivergentCalibration(CulturalCalibration):
    """
    Base class for neurodivergent communication patterns

    Key differences from neurotypical:
    - Different biological optimization parameters (km, ki)
    - Stronger or weaker cross-dimensional coupling
    - Different expected pattern signatures
    - May prioritize different dimensions
    """

    def __init__(self, neurodivergence_type: NeurodivergenceType):
        self.neurodivergence_type = neurodivergence_type

        # Base parameters - overridden by specific subclasses
        super().__init__(
            name=f"Neurodivergent ({neurodivergence_type.value})",
            description="Base neurodivergent communication calibration",
            km=0.35,
            ki=0.65,
            coupling_strength=0.25,
            expected_patterns={
                'reasoning': 'may show different logical patterns',
                'moral_expression': 'emotional regulation may differ',
                'social_architecture': 'different belonging signals',
                'wisdom_integration': 'pattern-based rather than narrative'
            },
            breathing_pattern="variable - atypical pause and rhythm patterns"
        )


class AutismSpectrumCalibration(NeurodivergentCalibration):
    """
    Autism spectrum communication patterns

    Research-based characteristics:
    - Higher priority on logical consistency (Ψ) over social harmony (f)
    - More direct moral expression (q) with less performative filtering
    - Pattern-based wisdom integration (ρ)
    - Different social belonging signals (f)
    - May have different saturation curves for emotional activation
    """

    def __init__(self):
        super().__init__(NeurodivergenceType.AUTISM_SPECTRUM)

        # Autism-specific calibration
        self.name = "Autism Spectrum Communication"
        self.description = "Calibration for autism spectrum communication patterns"

        # Biological parameters
        self.km = 0.45  # Higher saturation threshold - may tolerate more q before saturation
        self.ki = 3.5   # Higher inhibition threshold - less automatic filtering

        # Cross-dimensional coupling
        self.coupling_strength = 0.20  # Moderate coupling

        # Expected patterns
        self.expected_patterns = {
            'reasoning': 'High logical consistency priority - may value Ψ > f',
            'moral_expression': 'Direct and honest - less social performance filtering',
            'social_architecture': 'Different belonging signals - clarity over harmony',
            'wisdom_integration': 'Pattern-recognition based - systematic rather than narrative',
            'emotional_regulation': 'May show delayed or intense emotional expression',
            'communication_style': 'Precise language, literal interpretation common'
        }

        self.breathing_pattern = "detailed - may include extensive contextual information"

        # Dimension priorities (weights when ambiguous)
        self.dimension_priorities = {
            'psi': 1.3,  # Higher weight on internal consistency
            'rho': 1.1,  # Pattern-based wisdom valued
            'q': 0.9,    # Direct but may be filtered less
            'f': 0.7     # Social harmony weighted lower
        }


class ADHDCalibration(NeurodivergentCalibration):
    """
    ADHD communication patterns

    Research-based characteristics:
    - Rapid associative connections (high ρ variability)
    - High q activation with quick shifts
    - Non-linear thought patterns (Ψ may appear lower but is internally consistent)
    - High f-dimension engagement (relationship-focused)
    - Variable attention creates different temporal patterns
    """

    def __init__(self):
        super().__init__(NeurodivergenceType.ADHD)

        # ADHD-specific calibration
        self.name = "ADHD Communication"
        self.description = "Calibration for ADHD communication patterns"

        # Biological parameters
        self.km = 0.25  # Lower saturation threshold - faster activation
        self.ki = 1.2   # Lower inhibition - less automatic filtering

        # Cross-dimensional coupling
        self.coupling_strength = 0.35  # Higher coupling - dimensions interact more

        # Expected patterns
        self.expected_patterns = {
            'reasoning': 'Associative rather than linear - may appear fragmented but internally coherent',
            'moral_expression': 'Intense and variable - rapid emotional shifts',
            'social_architecture': 'High engagement with relationships and connection',
            'wisdom_integration': 'Associative leaps - connects distant concepts',
            'attention_pattern': 'Hyperfocus alternates with distributed attention',
            'communication_style': 'Rapid idea generation, topic shifting'
        }

        self.breathing_pattern = "rapid bursts - high energy shifts with pauses"

        # Dimension priorities
        self.dimension_priorities = {
            'psi': 0.8,  # May appear lower due to associative style
            'rho': 1.2,  # Rich associative connections
            'q': 1.4,    # High emotional activation
            'f': 1.3     # Strong relationship focus
        }


class HighStressTraumaCalibration(NeurodivergentCalibration):
    """
    High-stress/trauma-informed communication calibration

    CRITICAL for DEA/law enforcement application. Officers and agents
    operating under chronic stress show different communication patterns.

    Research-based characteristics:
    - Heightened threat detection (affects q interpretation)
    - Compressed/tactical communication (affects ρ and Ψ)
    - Different emotional regulation under stress
    - May prioritize clarity and directness over social niceties
    """

    def __init__(self):
        super().__init__(NeurodivergenceType.HIGH_STRESS_TRAUMA)

        # High-stress calibration
        self.name = "High-Stress/Trauma-Informed Communication"
        self.description = "Calibration for communication under chronic stress or trauma"

        # Biological parameters
        self.km = 0.20  # Very low saturation - quick activation under stress
        self.ki = 0.8   # Low inhibition - heightened vigilance

        # Cross-dimensional coupling
        self.coupling_strength = 0.40  # High coupling - stress affects all dimensions

        # Expected patterns
        self.expected_patterns = {
            'reasoning': 'Tactical and compressed - efficiency prioritized',
            'moral_expression': 'May be guarded or intense - threat-aware',
            'social_architecture': 'In-group/out-group distinction heightened',
            'wisdom_integration': 'Experience-based - survival knowledge',
            'emotional_regulation': 'May show hypervigilance or numbing',
            'communication_style': 'Direct, clear, action-oriented'
        }

        self.breathing_pattern = "tactical - short bursts with heightened awareness"

        # Dimension priorities
        self.dimension_priorities = {
            'psi': 1.1,  # Consistency valued for predictability
            'rho': 1.2,  # Experience-based wisdom
            'q': 1.5,    # Heightened emotional vigilance
            'f': 1.3     # Strong in-group cohesion
        }

        # Stress indicators (for real-time monitoring)
        self.stress_indicators = {
            'vocabulary': ['threat', 'danger', 'watch', 'careful', 'aware'],
            'temporal_compression': 0.3,  # Low τ - immediate focus
            'moral_activation_threshold': 0.4  # Lower threshold for q activation
        }


def test_neurodivergent_calibrations():
    """Test different neurodivergent calibrations"""

    print("=" * 90)
    print("NEURODIVERGENT COMMUNICATION CALIBRATIONS")
    print("=" * 90)
    print("\nCritical for DEA Human Performance Services Application")
    print("Law enforcement populations include significant neurodivergent representation\n")

    calibrations = [
        AutismSpectrumCalibration(),
        ADHDCalibration(),
        HighStressTraumaCalibration()
    ]

    for cal in calibrations:
        print("─" * 90)
        print(f"🧠 {cal.name}")
        print("─" * 90)
        print(f"Type: {cal.neurodivergence_type.value}")
        print(f"Description: {cal.description}")
        print(f"\nBiological Optimization Parameters:")
        print(f"  km (Saturation Midpoint):    {cal.km:.2f}")
        print(f"  ki (Inhibition Threshold):   {cal.ki:.2f}")
        print(f"  Coupling Strength:           {cal.coupling_strength:.2f}")
        print(f"\nBreathing Pattern: {cal.breathing_pattern}")

        print(f"\nExpected Communication Patterns:")
        for pattern_type, description in cal.expected_patterns.items():
            print(f"  • {pattern_type:25} {description}")

        if hasattr(cal, 'dimension_priorities'):
            print(f"\nDimension Priorities (when ambiguous):")
            for dim, weight in cal.dimension_priorities.items():
                bar = '█' * int(weight * 20)
                print(f"  {dim:5} {weight:.1f} {bar}")

        print()

    print("=" * 90)
    print("KEY INSIGHTS FOR DEA APPLICATION:")
    print("=" * 90)
    print("""
1. AUTISM SPECTRUM OFFICERS:
   - May prioritize logical consistency over social harmony
   - Direct communication should not be misinterpreted as hostility
   - Pattern recognition abilities can be asset in investigation

2. ADHD OFFICERS:
   - Rapid associative thinking can generate creative solutions
   - Topic shifts are cognitive style, not lack of focus
   - Hyperfocus states can be extremely productive

3. HIGH-STRESS/TRAUMA CONTEXT:
   - Heightened threat detection affects q-dimension interpretation
   - Tactical communication is adaptive, not pathological
   - In-group cohesion (f) is survival mechanism

CRITICAL: Rose Glass v2 with these calibrations enables:
- Accurate translation of neurodivergent communication
- Avoids pathologizing adaptive patterns
- Identifies when to adjust synthetic response strategies
- Real-time stress monitoring through dimensional shifts
    """)
    print("=" * 90)


if __name__ == "__main__":
    test_neurodivergent_calibrations()
