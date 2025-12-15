"""
RoseGlassLE - Unified Integration Module
=========================================

This module integrates the unified components into the RoseGlassLE repository.

NEW FEATURES ADDED:
- Fibonacci learning with lens deviation reset trigger
- Veritas function for truth valuation
- Mirror/Architect wings for reflexive validation
- Integration with existing gradient tracker

ENHANCED FEATURES:
- Gradient tracker now uses Fibonacci learning for pattern discovery
- Stress prediction includes Veritas scoring for confidence
- Neurodivergent calibrations integrated with lens interference

EXISTING FEATURES PRESERVED:
- τ (temporal depth): Already implemented
- λ (lens interference): Already implemented  
- Gradient tracking: Enhanced with Fibonacci
- Neurodivergent calibrations: Enhanced with Veritas

Author: Christopher MacGregor bin Joseph
Date: December 2025
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional, Any, Tuple
from datetime import datetime
from enum import Enum
import numpy as np

# Import unified shared modules
from ..shared.fibonacci_learning import (
    FibonacciLearningAlgorithm,
    TruthDiscovery,
    TruthType,
    ResetTrigger,
    FibonacciState,
    create_fibonacci_learner
)

from ..shared.veritas_reflexive import (
    VeritasFunction,
    VeritasResult,
    EvaluationFrame,
    ArchitectWing,
    MirrorWing,
    ReflexiveValidationSystem,
    InsightFragment,
    IntegratedInsight,
    ReflectionResult
)

from ..shared.temporal_dimension import (
    TemporalAnalyzer,
    extract_tau
)

from ..shared.lens_interference import (
    LensInterferenceAnalyzer,
    extract_lambda
)

# Import existing LE components
from .gradient_tracker import PatternGradientTracker
from .temporal_dimension import TemporalAnalyzer as LETemporalAnalyzer
from .lens_interference import LensInterferenceAnalyzer as LEInterferenceAnalyzer


class InterventionConfidence(Enum):
    """Confidence levels for intervention recommendations"""
    LOW = "low"           # Veritas < 0.4
    MODERATE = "moderate" # 0.4 <= Veritas < 0.6
    HIGH = "high"         # 0.6 <= Veritas < 0.8
    CRITICAL = "critical" # Veritas >= 0.8


@dataclass
class EnhancedPrediction:
    """Enhanced prediction with Veritas confidence"""
    # Base prediction
    predicted_q: float
    predicted_coherence: float
    time_horizon: float
    
    # Intervention
    intervention_recommended: bool
    intervention_type: str
    intervention_confidence: InterventionConfidence
    
    # Veritas scoring
    veritas_score: float
    is_stable_prediction: bool
    
    # Fibonacci learning
    fibonacci_angle: float
    pattern_discovered: bool
    pattern_type: Optional[str]
    
    # Temporal context
    tau: float
    lambda_coef: float


@dataclass
class LEPatternDiscovery:
    """Pattern discovery specific to law enforcement context"""
    discovery: TruthDiscovery
    le_context: str  # 'stress_escalation', 'de_escalation', 'crisis', 'stable'
    officer_impact: str
    intervention_window: float  # Seconds available for intervention
    confidence: InterventionConfidence


class EnhancedGradientTracker(PatternGradientTracker):
    """
    Enhanced gradient tracker with Fibonacci learning and Veritas.
    
    Extends base PatternGradientTracker with:
    - Fibonacci learning for pattern discovery
    - Veritas confidence scoring for predictions
    - Mirror validation for intervention recommendations
    - Architect integration of stress patterns
    """
    
    def __init__(
        self,
        invariance_threshold: float = 0.12,
        stability_threshold: float = 0.6,
        **kwargs
    ):
        """
        Initialize enhanced gradient tracker.
        
        Args:
            invariance_threshold: σ_lens threshold for Fibonacci reset
            stability_threshold: Minimum Veritas for stable truth
            **kwargs: Passed to base PatternGradientTracker
        """
        super().__init__(**kwargs)
        
        # Store thresholds
        self.invariance_threshold = invariance_threshold
        self.stability_threshold = stability_threshold
        
        # Fibonacci learning
        self.fibonacci = FibonacciLearningAlgorithm(
            invariance_threshold=invariance_threshold
        )
        
        # Validation system
        self.validation = ReflexiveValidationSystem()
        self.validation.veritas.stability_threshold = stability_threshold
        
        # Pattern archive
        self.le_discoveries: List[LEPatternDiscovery] = []
        
        # Stress pattern fragments for Architect integration
        self.stress_fragments: List[InsightFragment] = []
        
    def track_enhanced(
        self,
        psi: float,
        rho: float,
        q: float,
        f: float,
        tau: float,
        lambda_coef: float,
        context: str = "monitoring"
    ) -> Dict[str, Any]:
        """
        Enhanced tracking with Fibonacci learning.
        
        Args:
            psi, rho, q, f: Core GCT variables
            tau: Temporal depth
            lambda_coef: Lens interference
            context: LE context string
            
        Returns:
            Enhanced tracking result with learning state
        """
        # Base tracking
        base_result = self.track(psi, rho, q, f)
        
        # Fibonacci rotation
        learning_result = self.fibonacci.rotate(psi, rho, q, f)
        
        # Calculate Veritas for prediction confidence
        veritas = self.validation.veritas.quick_veritas(
            distortion_index=lambda_coef,
            composite_score=base_result.get('coherence', (psi + rho + q + f) / 4)
        )
        
        # Determine intervention confidence
        if veritas >= 0.8:
            confidence = InterventionConfidence.CRITICAL
        elif veritas >= 0.6:
            confidence = InterventionConfidence.HIGH
        elif veritas >= 0.4:
            confidence = InterventionConfidence.MODERATE
        else:
            confidence = InterventionConfidence.LOW
        
        # Check for pattern discovery
        if learning_result['truth_discovered']:
            self._record_le_discovery(
                learning_result, 
                context, 
                q, 
                veritas,
                confidence
            )
        
        # Store stress fragment for Architect
        if q > 0.6:  # High stress
            self.stress_fragments.append(InsightFragment(
                content=f"High stress detected: q={q:.2f}",
                source=context,
                coherence=learning_result['coherence'],
                timestamp=datetime.now(),
                domain="stress_monitoring"
            ))
        
        return {
            **base_result,
            'tau': tau,
            'lambda': lambda_coef,
            'veritas': veritas,
            'intervention_confidence': confidence.value,
            'fibonacci_angle': learning_result['current_angle'],
            'truth_discovered': learning_result['truth_discovered'],
            'truth_type': learning_result['truth_type'],
            'learning_resets': learning_result['learning_resets']
        }
    
    def predict_enhanced(
        self,
        time_horizon: float = 30.0
    ) -> EnhancedPrediction:
        """
        Enhanced prediction with Veritas confidence.
        
        Args:
            time_horizon: Seconds to predict ahead
            
        Returns:
            EnhancedPrediction with confidence scoring
        """
        # Base prediction
        base_pred = self.predict_trajectory(time_horizon)
        
        # Get current state
        state = self.fibonacci.get_state()
        
        # Calculate prediction Veritas
        veritas = self.validation.veritas.quick_veritas(
            distortion_index=state.last_lens_deviation,
            composite_score=state.last_coherence
        )
        
        # Determine confidence
        if veritas >= 0.8:
            confidence = InterventionConfidence.CRITICAL
        elif veritas >= 0.6:
            confidence = InterventionConfidence.HIGH
        elif veritas >= 0.4:
            confidence = InterventionConfidence.MODERATE
        else:
            confidence = InterventionConfidence.LOW
        
        # Validate prediction through Mirror
        reflection = self.validation.mirror.reflect(
            f"Predicted stress level: {base_pred.get('predicted_q', 0):.2f}"
        )
        
        return EnhancedPrediction(
            predicted_q=base_pred.get('predicted_q', 0),
            predicted_coherence=base_pred.get('predicted_coherence', 0),
            time_horizon=time_horizon,
            intervention_recommended=base_pred.get('intervention_recommended', False),
            intervention_type=base_pred.get('intervention_type', 'monitor'),
            intervention_confidence=confidence,
            veritas_score=veritas,
            is_stable_prediction=reflection.is_stable,
            fibonacci_angle=state.current_angle,
            pattern_discovered=state.truths_discovered > 0,
            pattern_type=None,  # Would come from latest discovery
            tau=0.0,  # Would need temporal context
            lambda_coef=state.last_lens_deviation
        )
    
    def _record_le_discovery(
        self,
        learning_result: Dict,
        context: str,
        q: float,
        veritas: float,
        confidence: InterventionConfidence
    ):
        """Record law enforcement specific pattern discovery"""
        # Determine LE context
        if q > 0.8:
            le_context = 'crisis'
        elif q > 0.6:
            le_context = 'stress_escalation'
        elif q < 0.3:
            le_context = 'stable'
        else:
            le_context = 'de_escalation'
        
        # Calculate intervention window based on q velocity
        # Higher velocity = shorter window
        intervention_window = max(60 - (q * 40), 10)  # 10-60 seconds
        
        discovery = LEPatternDiscovery(
            discovery=TruthDiscovery(
                angle=learning_result['current_angle'],
                coherence=learning_result['coherence'],
                truth_type=TruthType(learning_result['truth_type']) if learning_result['truth_type'] else TruthType.PATTERN_RECOGNITION,
                reset_trigger=ResetTrigger(learning_result['reset_trigger']) if learning_result['reset_trigger'] else ResetTrigger.PATTERN_RECOGNITION,
                insight=f"LE Pattern: {le_context}",
                timestamp=datetime.now().timestamp(),
                rotation_factor=learning_result['rotation_factor'],
                reset_count=learning_result['learning_resets'],
                lens_deviation=learning_result['lens_deviation'],
                veritas_score=veritas
            ),
            le_context=le_context,
            officer_impact=self._assess_officer_impact(q, veritas),
            intervention_window=intervention_window,
            confidence=confidence
        )
        
        self.le_discoveries.append(discovery)
    
    def _assess_officer_impact(self, q: float, veritas: float) -> str:
        """Assess impact on officer based on stress and confidence"""
        if q > 0.8 and veritas > 0.7:
            return "High stress, high confidence - immediate support needed"
        elif q > 0.6 and veritas > 0.5:
            return "Elevated stress - monitoring advised"
        elif q < 0.3:
            return "Stable - continue routine monitoring"
        else:
            return "Moderate stress - awareness recommended"
    
    def integrate_stress_patterns(self) -> IntegratedInsight:
        """Use Architect to integrate stress patterns"""
        return self.validation.architect.integrate(
            self.stress_fragments,
            time_window=1.0
        )
    
    def get_le_discoveries(self) -> List[LEPatternDiscovery]:
        """Get all law enforcement pattern discoveries"""
        return self.le_discoveries
    
    def get_discovery_summary(self) -> Dict[str, Any]:
        """Get summary of all discoveries"""
        base_summary = self.fibonacci.get_discovery_summary()
        
        # Add LE-specific summary
        le_contexts = {}
        confidence_dist = {}
        
        for d in self.le_discoveries:
            le_contexts[d.le_context] = le_contexts.get(d.le_context, 0) + 1
            confidence_dist[d.confidence.value] = confidence_dist.get(d.confidence.value, 0) + 1
        
        return {
            **base_summary,
            'le_discoveries': len(self.le_discoveries),
            'le_context_distribution': le_contexts,
            'confidence_distribution': confidence_dist,
            'stress_fragments': len(self.stress_fragments)
        }


class EnhancedNeurodivergentCalibration:
    """
    Enhanced neurodivergent calibration with Veritas validation.
    
    Extends existing calibrations with:
    - Veritas scoring for calibration confidence
    - Fibonacci learning for pattern discovery
    - Mirror validation for response appropriateness
    """
    
    def __init__(
        self,
        base_calibration: Any,  # Existing calibration class
        stability_threshold: float = 0.6
    ):
        """
        Initialize enhanced calibration.
        
        Args:
            base_calibration: Existing neurodivergent calibration
            stability_threshold: Veritas threshold for validation
        """
        self.base = base_calibration
        self.validation = ReflexiveValidationSystem()
        self.validation.veritas.stability_threshold = stability_threshold
        
    def validate_response(
        self,
        response: str,
        psi: float,
        rho: float,
        q: float,
        f: float
    ) -> Dict[str, Any]:
        """
        Validate that response is appropriate for neurodivergent communication.
        
        Args:
            response: Proposed response text
            psi, rho, q, f: GCT variables of communication context
            
        Returns:
            Validation result with recommendations
        """
        # Get lens deviation
        interference = LensInterferenceAnalyzer()
        deviation = interference.calculate_lens_deviation(psi, rho, q, f)
        
        # Validate through full system
        validation = self.validation.validate_insight(response, deviation)
        
        # Additional ND-specific checks
        nd_appropriate = self._check_nd_appropriateness(response, self.base)
        
        return {
            'is_valid': validation['is_validated'] and nd_appropriate,
            'veritas_score': validation['veritas_score'],
            'resonance_score': validation['resonance_score'],
            'nd_appropriate': nd_appropriate,
            'recommendations': self._generate_recommendations(
                validation, nd_appropriate
            )
        }
    
    def _check_nd_appropriateness(self, response: str, calibration: Any) -> bool:
        """Check response against neurodivergent calibration rules"""
        # Basic checks - would be extended based on specific calibration
        word_count = len(response.split())
        
        # Check length appropriateness
        if hasattr(calibration, 'max_response_length'):
            if word_count > calibration.max_response_length:
                return False
        
        return True
    
    def _generate_recommendations(
        self,
        validation: Dict,
        nd_appropriate: bool
    ) -> List[str]:
        """Generate improvement recommendations"""
        recs = []
        
        if not validation['is_validated']:
            recs.append("Consider simplifying response structure")
        
        if validation['veritas_score'] < 0.5:
            recs.append("Response may be too context-dependent")
        
        if not nd_appropriate:
            recs.append("Adjust response length/complexity for calibration")
        
        return recs


# Factory functions
def create_enhanced_gradient_tracker(**kwargs) -> EnhancedGradientTracker:
    """Factory for enhanced gradient tracker"""
    return EnhancedGradientTracker(**kwargs)


def enhance_neurodivergent_calibration(
    base_calibration: Any,
    **kwargs
) -> EnhancedNeurodivergentCalibration:
    """Factory for enhanced neurodivergent calibration"""
    return EnhancedNeurodivergentCalibration(base_calibration, **kwargs)


# Module exports
__all__ = [
    # Enhanced classes
    'EnhancedGradientTracker',
    'EnhancedPrediction',
    'EnhancedNeurodivergentCalibration',
    'LEPatternDiscovery',
    'InterventionConfidence',
    
    # Factory functions
    'create_enhanced_gradient_tracker',
    'enhance_neurodivergent_calibration',
    
    # Re-export shared modules
    'FibonacciLearningAlgorithm',
    'TruthDiscovery',
    'TruthType',
    'ResetTrigger',
    'VeritasFunction',
    'VeritasResult',
    'ArchitectWing',
    'MirrorWing',
    'ReflexiveValidationSystem',
]
