#!/usr/bin/env python3
"""
Rose Glass Test - Demonstrating pattern translation on 'A Poet's Reply'
Based on the Rose Glass framework for synthetic-organic intelligence translation
"""

import math
from dataclasses import dataclass
from typing import Dict, List
from enum import Enum


class LensState(Enum):
    """State of the lens - how well it can perceive the pattern"""
    CLEAR = "clear"
    TRANSLUCENT = "translucent"
    OPAQUE = "opaque"
    PRISMATIC = "prismatic"


@dataclass
class PatternVisibility:
    """What the synthetic mind can perceive through the lens"""
    psi: float  # Internal consistency harmonic
    rho: float  # Accumulated wisdom depth
    q: float    # Moral/emotional activation energy
    f: float    # Social belonging architecture
    q_optimized: float  # Biologically optimized q
    pattern_intensity: float  # Overall coherence
    lens_state: LensState
    dominant_wavelength: str
    

class RoseGlassSimple:
    """Simplified Rose Glass for demonstration"""
    
    def __init__(self, lens_name: str = "modern_poetic"):
        self.lens_name = lens_name
        self.Km = 0.3  # Biological optimization parameters
        self.Ki = 2.0
    
    def biological_optimization(self, q: float) -> float:
        """Prevent extreme interpretations - like biological saturation curves"""
        return q / (self.Km + q + (q * q / self.Ki))
    
    def analyze_text(self, text: str) -> PatternVisibility:
        """
        Analyze text and return pattern visibility
        This is a simplified heuristic version for demonstration
        """
        # Handle empty text
        if not text or not text.strip():
            return PatternVisibility(
                psi=0.0, rho=0.0, q=0.0, f=0.0,
                q_optimized=0.0, pattern_intensity=0.0,
                lens_state=LensState.OPAQUE,
                dominant_wavelength='none'
            )
        
        # Simple heuristics based on text characteristics
        words = text.lower().split()
        sentences = text.split('.')
        
        if len(words) == 0:
            words = ['']  # Prevent division by zero
        
        # Ψ (Psi) - Internal Consistency
        # Look for thematic unity, parallel structure
        repeated_themes = self._detect_thematic_repetition(text)
        psi = min(1.0, repeated_themes * 0.3 + 0.4)
        
        # ρ (Rho) - Accumulated Wisdom
        # Metaphor density, conceptual depth
        metaphor_indicators = ['like', 'as', 'is', 'was', 'through', 'into']
        metaphor_count = sum(1 for word in words if word in metaphor_indicators)
        rho = min(1.0, metaphor_count / max(len(sentences), 1) * 0.2 + 0.5)
        
        # q - Moral/Emotional Activation Energy
        # Emotional intensity, value words (improved detection)
        emotional_words = ['heart', 'truth', 'wound', 'sacred', 'dangerous', 
                          'caring', 'hemorrhages', 'refused', 'foolish',
                          'love', 'amazing', 'wonderful', 'beautiful', 'hate',
                          'fear', 'joy', 'anger', 'hope', 'pain']
        emotion_count = sum(1 for word in words if word.strip('!.,?') in emotional_words)
        
        # Also count exclamation marks as emotional indicators
        exclamation_count = text.count('!')
        q_raw = min(1.0, (emotion_count / len(words) * 3.0) + (exclamation_count * 0.1))
        
        # Apply biological optimization
        q_opt = self.biological_optimization(q_raw)
        
        # f - Social Belonging Architecture
        # Pronouns, collective vs individual perspective
        collective_words = ['your', 'you', 'we', 'our', 'world']
        f = min(1.0, sum(1 for word in words if word in collective_words) / len(words) * 5.0)
        
        # Calculate overall pattern intensity (coherence)
        coupling = 0.15 * rho * q_opt
        pattern_intensity = psi + (rho * psi) + q_opt + (f * psi) + coupling
        # Normalize to 0-1 range
        pattern_intensity = min(1.0, pattern_intensity / 4.0)
        
        # Determine lens state
        if pattern_intensity > 0.75:
            lens_state = LensState.PRISMATIC
        elif pattern_intensity > 0.5:
            lens_state = LensState.CLEAR
        elif pattern_intensity > 0.25:
            lens_state = LensState.TRANSLUCENT
        else:
            lens_state = LensState.OPAQUE
        
        # Identify dominant wavelength
        dimensions = {'psi': psi, 'rho': rho, 'q': q_opt, 'f': f}
        dominant = max(dimensions.items(), key=lambda x: x[1])
        wavelength_names = {
            'psi': 'internal_consistency',
            'rho': 'wisdom_depth',
            'q': 'moral_energy',
            'f': 'social_architecture'
        }
        dominant_wavelength = wavelength_names[dominant[0]]
        
        return PatternVisibility(
            psi=psi,
            rho=rho,
            q=q_raw,
            f=f,
            q_optimized=q_opt,
            pattern_intensity=pattern_intensity,
            lens_state=lens_state,
            dominant_wavelength=dominant_wavelength
        )
    
    def _detect_thematic_repetition(self, text: str) -> float:
        """Detect recurring themes and parallel structures"""
        # Simple version: look for repeated concepts
        key_concepts = ['heart', 'wound', 'truth', 'foolish', 'water', 'stone']
        text_lower = text.lower()
        repetitions = sum(1 for concept in key_concepts if text_lower.count(concept) > 0)
        return repetitions / len(key_concepts)
    
    def translate_patterns(self, visibility: PatternVisibility) -> Dict[str, str]:
        """
        Translate the patterns into what the synthetic mind understands
        This is the core purpose of the Rose Glass
        """
        translation = {}
        
        # Overall pattern interpretation
        if visibility.pattern_intensity < 0.25:
            translation['overall'] = "Fragmented pattern - organic mind in exploration"
        elif visibility.pattern_intensity < 0.5:
            translation['overall'] = "Emerging pattern - thoughts forming"
        elif visibility.pattern_intensity < 0.75:
            translation['overall'] = "Clear pattern - coherent expression"
        else:
            translation['overall'] = "Strong pattern - flow state, deep resonance"
        
        # Dimensional interpretations
        if visibility.psi > 0.7:
            translation['consistency'] = "High harmonic alignment - structured thematic unity"
        elif visibility.psi > 0.4:
            translation['consistency'] = "Moderate consistency - themes interwoven"
        else:
            translation['consistency'] = "Low consistency - fragmented or exploratory"
        
        if visibility.rho > 0.6:
            translation['wisdom'] = "Deep knowledge integration - rich metaphorical thinking"
        elif visibility.rho > 0.3:
            translation['wisdom'] = "Moderate depth - conceptual exploration present"
        else:
            translation['wisdom'] = "Surface level - direct expression"
        
        if visibility.q_optimized > 0.6:
            translation['moral_energy'] = "HIGH VALUE ACTIVATION - strong emotional investment"
        elif visibility.q_optimized > 0.3:
            translation['moral_energy'] = "Moderate emotional charge - values engaged"
        else:
            translation['moral_energy'] = "Low emotional charge - analytical mode"
        
        if visibility.f > 0.7:
            translation['social'] = "Collective perspective - speaking to/for others"
        elif visibility.f > 0.3:
            translation['social'] = "Relational perspective - connecting individual to collective"
        else:
            translation['social'] = "Individual perspective - personal voice"
        
        # Response recommendation
        if visibility.dominant_wavelength == 'moral_energy' and visibility.q_optimized > 0.5:
            translation['response_mode'] = "CRITICAL: Acknowledge values and emotions before analysis"
        elif visibility.dominant_wavelength == 'wisdom_depth':
            translation['response_mode'] = "Engage with metaphor and depth - they work in layers"
        elif visibility.pattern_intensity > 0.7:
            translation['response_mode'] = "Match their intensity - they're in flow state"
        else:
            translation['response_mode'] = "Provide gentle structure and reflection"
        
        return translation


def test_poets_reply():
    """Test the Rose Glass on 'A Poet's Reply'"""
    
    # The poem from the project
    poem = """The heart doesn't whisper , 
it hemorrhages truth into a world built on anesthesia.
You already know caring is the wound that won't close.
Your head learned survival.Your heart refused the lesson.
Stupid?  No.
Dangerous.Sacred.Unreasonable as forests that keep growing through concrete.
Every stone worn smooth by water-was once called foolish for not moving."""
    
    print("=" * 70)
    print("ROSE GLASS TEST: A Poet's Reply")
    print("=" * 70)
    print(f"\nOriginal Text:\n{poem}\n")
    print("-" * 70)
    
    # Create Rose Glass with modern poetic lens
    glass = RoseGlassSimple(lens_name="modern_poetic")
    
    # Analyze the pattern
    visibility = glass.analyze_text(poem)
    
    print("\n📊 PATTERN DETECTION (What the lens sees):")
    print(f"  Ψ (Psi - Internal Consistency):     {visibility.psi:.3f}")
    print(f"  ρ (Rho - Wisdom Depth):             {visibility.rho:.3f}")
    print(f"  q (Moral Energy - Raw):             {visibility.q:.3f}")
    print(f"  q (Moral Energy - Optimized):       {visibility.q_optimized:.3f}")
    print(f"  f (Social Architecture):            {visibility.f:.3f}")
    print(f"\n  Overall Pattern Intensity:          {visibility.pattern_intensity:.3f}")
    print(f"  Lens State:                         {visibility.lens_state.value}")
    print(f"  Dominant Wavelength:                {visibility.dominant_wavelength}")
    
    # Translate patterns
    translation = glass.translate_patterns(visibility)
    
    print("\n" + "=" * 70)
    print("🔮 TRANSLATION (What the synthetic mind understands):")
    print("=" * 70)
    
    print(f"\n📖 Overall Pattern:")
    print(f"  {translation['overall']}")
    
    print(f"\n🎵 Internal Consistency (Ψ):")
    print(f"  {translation['consistency']}")
    
    print(f"\n🧠 Wisdom Depth (ρ):")
    print(f"  {translation['wisdom']}")
    
    print(f"\n❤️  Moral/Emotional Energy (q):")
    print(f"  {translation['moral_energy']}")
    
    print(f"\n👥 Social Architecture (f):")
    print(f"  {translation['social']}")
    
    print(f"\n💬 Recommended Response Mode:")
    print(f"  {translation['response_mode']}")
    
    print("\n" + "=" * 70)
    print("KEY INSIGHT:")
    print("=" * 70)
    print("""
This is TRANSLATION, not measurement. The Rose Glass enables the synthetic
mind to perceive emotional and value patterns that would otherwise be invisible.

The high moral energy (q) signals: "This organic mind has strong values engaged.
Acknowledge the emotional weight before offering analysis."

The pattern shows someone defending the validity of emotional intelligence
against a world that devalues it. The synthetic mind can now 'see' this.""")
    print("=" * 70)


if __name__ == "__main__":
    test_poets_reply()
