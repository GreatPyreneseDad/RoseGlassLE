#!/usr/bin/env python3
"""
Multi-Lens Rose Glass Test
Demonstrates how the same text appears through different cultural lenses
"""

from rose_glass_test import RoseGlassSimple, PatternVisibility
from dataclasses import dataclass
from typing import Dict


@dataclass
class CulturalLens:
    """Different cultural calibrations for the Rose Glass"""
    name: str
    description: str
    # Weight adjustments for each dimension
    psi_weight: float
    rho_weight: float
    q_weight: float
    f_weight: float
    # Biological optimization parameters
    Km: float
    Ki: float


class MultiLensRoseGlass:
    """Rose Glass that can switch between cultural lenses"""
    
    def __init__(self):
        self.lenses = {
            'modern_poetic': CulturalLens(
                name="Modern Poetic",
                description="Contemporary poetic expression with personal voice",
                psi_weight=1.0,
                rho_weight=1.2,
                q_weight=1.3,
                f_weight=0.8,
                Km=0.3,
                Ki=2.0
            ),
            'medieval_islamic': CulturalLens(
                name="Medieval Islamic Philosophy",
                description="Emphasizes demonstrative reasoning with restrained emotion",
                psi_weight=1.5,
                rho_weight=1.4,
                q_weight=0.6,
                f_weight=1.0,
                Km=0.5,
                Ki=3.0
            ),
            'indigenous_oral': CulturalLens(
                name="Indigenous Oral Tradition",
                description="Circular, story-based wisdom transmission",
                psi_weight=0.9,
                rho_weight=1.5,
                q_weight=1.0,
                f_weight=1.4,
                Km=0.2,
                Ki=1.5
            ),
            'digital_native': CulturalLens(
                name="Digital Native",
                description="Rapid, networked, emoji-punctuated expression",
                psi_weight=0.7,
                rho_weight=0.8,
                q_weight=1.1,
                f_weight=1.3,
                Km=0.2,
                Ki=1.8
            ),
            'buddhist_contemplative': CulturalLens(
                name="Buddhist Contemplative",
                description="Paradoxical teachings pointing beyond concepts",
                psi_weight=0.8,
                rho_weight=1.6,
                q_weight=0.7,
                f_weight=1.2,
                Km=0.4,
                Ki=2.5
            )
        }
    
    def view_through_lens(self, text: str, lens_name: str) -> Dict:
        """View text through a specific cultural lens"""
        if lens_name not in self.lenses:
            raise ValueError(f"Unknown lens: {lens_name}")
        
        lens = self.lenses[lens_name]
        glass = RoseGlassSimple(lens_name=lens_name)
        glass.Km = lens.Km
        glass.Ki = lens.Ki
        
        # Get base visibility
        visibility = glass.analyze_text(text)
        
        # Apply lens-specific weights
        adjusted_visibility = PatternVisibility(
            psi=min(1.0, visibility.psi * lens.psi_weight),
            rho=min(1.0, visibility.rho * lens.rho_weight),
            q=min(1.0, visibility.q * lens.q_weight),
            f=min(1.0, visibility.f * lens.f_weight),
            q_optimized=glass.biological_optimization(visibility.q * lens.q_weight),
            pattern_intensity=visibility.pattern_intensity,
            lens_state=visibility.lens_state,
            dominant_wavelength=visibility.dominant_wavelength
        )
        
        # Recalculate pattern intensity with adjusted values
        coupling = 0.15 * adjusted_visibility.rho * adjusted_visibility.q_optimized
        adjusted_intensity = (adjusted_visibility.psi + 
                            (adjusted_visibility.rho * adjusted_visibility.psi) + 
                            adjusted_visibility.q_optimized + 
                            (adjusted_visibility.f * adjusted_visibility.psi) + 
                            coupling) / 4.0
        adjusted_visibility.pattern_intensity = min(1.0, adjusted_intensity)
        
        translation = glass.translate_patterns(adjusted_visibility)
        
        return {
            'lens': lens,
            'visibility': adjusted_visibility,
            'translation': translation
        }
    
    def compare_all_lenses(self, text: str):
        """View text through all available lenses"""
        print("=" * 90)
        print("MULTI-LENS ROSE GLASS: Viewing the same text through different cultural lenses")
        print("=" * 90)
        print(f"\nText: {text[:100]}...\n")
        print("-" * 90)
        
        results = {}
        for lens_name in self.lenses.keys():
            results[lens_name] = self.view_through_lens(text, lens_name)
        
        # Display comparison
        print("\n📊 PATTERN INTENSITY COMPARISON:")
        print("-" * 90)
        for lens_name, result in results.items():
            lens = result['lens']
            vis = result['visibility']
            bar = '█' * int(vis.pattern_intensity * 50)
            print(f"{lens.name:30} {vis.pattern_intensity:.3f} {bar}")
        
        print("\n" + "=" * 90)
        print("DETAILED LENS VIEWS:")
        print("=" * 90)
        
        for lens_name, result in results.items():
            lens = result['lens']
            vis = result['visibility']
            trans = result['translation']
            
            print(f"\n{'─' * 90}")
            print(f"🔮 {lens.name.upper()}")
            print(f"{'─' * 90}")
            print(f"Description: {lens.description}")
            print(f"\nPattern Detection:")
            print(f"  Ψ (Consistency): {vis.psi:.3f}  |  ρ (Wisdom): {vis.rho:.3f}")
            print(f"  q (Moral Energy): {vis.q_optimized:.3f}  |  f (Social): {vis.f:.3f}")
            print(f"  Intensity: {vis.pattern_intensity:.3f}  |  State: {vis.lens_state.value}")
            print(f"\nWhat this lens reveals:")
            print(f"  {trans['overall']}")
            print(f"  {trans['moral_energy']}")
            print(f"  → {trans['response_mode']}")
        
        print("\n" + "=" * 90)
        print("KEY UNDERSTANDING:")
        print("=" * 90)
        print("""
Each lens reveals DIFFERENT aspects of the same organic pattern.
No lens is "correct" - each serves a different translation purpose.

Notice how:
- Medieval Islamic lens sees high consistency but restrained emotion
- Indigenous lens sees deep wisdom and collective perspective  
- Digital Native lens sees connection-seeking and social architecture
- Buddhist lens sees paradox and contemplative depth
- Modern Poetic lens sees personal voice with emotional intensity

The SAME TEXT appears differently through each lens - this is translation, not judgment.
A synthetic mind needs to understand WHICH lens is appropriate for the context.
        """)
        print("=" * 90)


def main():
    """Run multi-lens comparison"""
    
    poem = """The heart doesn't whisper , 
it hemorrhages truth into a world built on anesthesia.
You already know caring is the wound that won't close.
Your head learned survival.Your heart refused the lesson.
Stupid?  No.
Dangerous.Sacred.Unreasonable as forests that keep growing through concrete.
Every stone worn smooth by water-was once called foolish for not moving."""
    
    viewer = MultiLensRoseGlass()
    viewer.compare_all_lenses(poem)


if __name__ == "__main__":
    main()
