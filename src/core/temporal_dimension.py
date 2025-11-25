#!/usr/bin/env python3
"""
Temporal Depth Dimension (τ - Tau)

Measures how much time is encoded in expression and how resistant
the meaning is to temporal decay. Addresses Gap 1 from testing analysis.

Key insight: Some expressions compress vast temporal wisdom (geological time,
generational knowledge) while others are ephemeral (trending content, immediate reactions).
"""

import re
from typing import List, Dict, Tuple
from dataclasses import dataclass


@dataclass
class TemporalSignature:
    """Signature of temporal depth in text"""
    compression_ratio: float  # How much time is compressed (0-1)
    decay_resistance: float   # How well meaning survives time (0-1)
    tau: float               # Overall temporal depth (0-1)
    temporal_markers: List[str]  # Detected temporal indicators
    timescale_category: str  # immediate, ephemeral, enduring, eternal


class TemporalAnalyzer:
    """
    Analyzes the temporal depth of communication

    τ = temporal_compression_ratio * decay_resistance

    High τ: Ancient wisdom texts, geological metaphors, generational stories
    Low τ: Twitter threads, trending hashtags, immediate reactions
    """

    def __init__(self):
        # Temporal compression indicators (how much time is referenced)
        self.eternal_markers = {
            'stone', 'water', 'mountain', 'ocean', 'forest', 'river',
            'stars', 'earth', 'generations', 'ancient', 'eternal',
            'timeless', 'ages', 'eons', 'millennia', 'always'
        }

        self.enduring_markers = {
            'tradition', 'wisdom', 'legacy', 'heritage', 'history',
            'ancestors', 'descendants', 'decades', 'centuries',
            'lasting', 'enduring', 'survived', 'weathered'
        }

        self.ephemeral_markers = {
            'trending', 'viral', 'breaking', 'just now', 'update',
            'latest', 'new', 'fresh', 'hot take', 'thread',
            'rn' , 'atm', 'today', 'currently', 'right now'
        }

        self.immediate_markers = {
            '!!!', '🔥', '💯', 'omg', 'wtf', 'lol', 'asap',
            'urgent', 'breaking', 'alert', 'now', 'quick'
        }

        # Decay resistance indicators (metaphorical vs literal)
        self.metaphor_patterns = [
            r'\b\w+\s+like\s+\w+',  # "stone like water"
            r'\b\w+\s+as\s+\w+',    # "smooth as water"
            r'\b\w+\s+through\s+\w+',  # "growing through concrete"
            r'\b\w+\s+into\s+\w+',  # "hemorrhages into"
            r'\b\w+\s+of\s+\w+',    # "forests of time"
        ]

        self.literal_patterns = [
            r'\d{1,2}:\d{2}',  # time stamps
            r'@\w+',           # mentions
            r'#\w+',           # hashtags
            r'http[s]?://',    # links
        ]

    def analyze(self, text: str) -> TemporalSignature:
        """
        Analyze temporal depth of text

        Returns TemporalSignature with:
        - compression_ratio: how much time is encoded
        - decay_resistance: how well it survives temporal distance
        - tau: overall temporal depth
        """
        text_lower = text.lower()
        words = set(text_lower.split())

        # Calculate compression ratio (0-1)
        eternal_count = sum(1 for m in self.eternal_markers if m in text_lower)
        enduring_count = sum(1 for m in self.enduring_markers if m in text_lower)
        ephemeral_count = sum(1 for m in self.ephemeral_markers if m in text_lower)
        immediate_count = sum(1 for m in self.immediate_markers if m in text_lower)

        # Weighted scoring
        compression_score = (
            (eternal_count * 1.0) +
            (enduring_count * 0.7) -
            (ephemeral_count * 0.5) -
            (immediate_count * 1.0)
        )

        # Normalize to 0-1 (scaling heuristic)
        total_markers = eternal_count + enduring_count + ephemeral_count + immediate_count
        if total_markers == 0:
            compression_ratio = 0.5  # neutral default
        else:
            compression_ratio = max(0.0, min(1.0, 0.5 + (compression_score / (total_markers * 2))))

        # Calculate decay resistance (0-1)
        metaphor_count = sum(1 for pattern in self.metaphor_patterns
                           if re.search(pattern, text_lower))
        literal_count = sum(1 for pattern in self.literal_patterns
                          if re.search(pattern, text))

        # Metaphorical expression resists temporal decay better than literal
        if metaphor_count + literal_count == 0:
            decay_resistance = 0.5  # neutral default
        else:
            decay_resistance = metaphor_count / (metaphor_count + literal_count + 1)

        # Calculate tau
        tau = compression_ratio * decay_resistance

        # Determine timescale category
        if tau > 0.7:
            category = "eternal"
        elif tau > 0.5:
            category = "enduring"
        elif tau > 0.3:
            category = "ephemeral"
        else:
            category = "immediate"

        # Collect detected markers
        detected_markers = []
        detected_markers.extend([m for m in self.eternal_markers if m in text_lower])
        detected_markers.extend([m for m in self.enduring_markers if m in text_lower])
        detected_markers.extend([m for m in self.ephemeral_markers if m in text_lower])
        detected_markers.extend([m for m in self.immediate_markers if m in text_lower])

        return TemporalSignature(
            compression_ratio=compression_ratio,
            decay_resistance=decay_resistance,
            tau=tau,
            temporal_markers=detected_markers[:10],  # Limit for readability
            timescale_category=category
        )

    def compare_temporal_depth(self, text1: str, text2: str) -> Dict:
        """Compare temporal depth of two texts"""
        sig1 = self.analyze(text1)
        sig2 = self.analyze(text2)

        return {
            'text1_tau': sig1.tau,
            'text2_tau': sig2.tau,
            'tau_difference': abs(sig1.tau - sig2.tau),
            'text1_category': sig1.timescale_category,
            'text2_category': sig2.timescale_category,
            'temporal_alignment': 1.0 - abs(sig1.tau - sig2.tau)
        }


def test_temporal_analyzer():
    """Test the temporal analyzer with different text types"""

    analyzer = TemporalAnalyzer()

    # Test texts with different temporal depths
    tests = {
        "Ancient Wisdom": """Every stone worn smooth by water was once called foolish
        for not moving. The mountain watches generations pass like clouds.""",

        "Twitter Thread": """OMG just saw the latest update!!! This is trending rn 🔥💯
        Thread incoming... #breaking #viral""",

        "Modern Poetry": """The heart doesn't whisper, it hemorrhages truth into a world
        built on anesthesia. Unreasonable as forests that keep growing through concrete.""",

        "News Update": """Breaking: Latest developments at 3:45 PM. Check link for updates.
        #news #update @source"""
    }

    print("=" * 80)
    print("TEMPORAL DEPTH ANALYSIS (τ - Tau)")
    print("=" * 80)

    for name, text in tests.items():
        sig = analyzer.analyze(text)
        print(f"\n{'─' * 80}")
        print(f"📖 {name}")
        print(f"{'─' * 80}")
        print(f"Text: {text[:100]}...")
        print(f"\nτ (Temporal Depth):      {sig.tau:.3f}")
        print(f"Compression Ratio:       {sig.compression_ratio:.3f}")
        print(f"Decay Resistance:        {sig.decay_resistance:.3f}")
        print(f"Timescale Category:      {sig.timescale_category}")
        if sig.temporal_markers:
            print(f"Temporal Markers:        {', '.join(sig.temporal_markers[:5])}")

    print("\n" + "=" * 80)
    print("KEY INSIGHTS:")
    print("=" * 80)
    print("""
τ (Tau) reveals how much time is compressed in expression:
- Ancient wisdom: high τ (geological time, generations)
- Modern poetry: moderate-high τ (metaphorical compression)
- Twitter content: low τ (immediate, ephemeral)
- News updates: very low τ (time-stamped, link-dependent)

This dimension was missing from Rose Glass v1 - it treats temporal dynamics
as static. τ enables tracking wisdom transmission across time.
    """)


if __name__ == "__main__":
    test_temporal_analyzer()
