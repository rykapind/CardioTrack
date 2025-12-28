"""
Arrhythmia detector module.
Version 1.0.0
"""

import numpy as np
import scipy.signal as sig

# Constants
SAMPLING_RATE = 250
WINDOW_SIZE = 256

def preprocess_ecg(raw_signal):
    """Apply bandpass filter and normalize."""
    # Design filter
    b, a = sig.butter(4, [0.5, 40], btype='band', fs=SAMPLING_RATE)
    filtered = sig.filtfilt(b, a, raw_signal)
    # Normalize
    normalized = (filtered - np.mean(filtered)) / np.std(filtered)
    return normalized

def detect_qrs(signal):
    """Detect QRS complexes using Pan-Tompkins algorithm."""
    # Simplified detection
    diff_signal = np.diff(signal)
    squared = diff_signal ** 2
    # Moving window integration
    window = np.ones(WINDOW_SIZE) / WINDOW_SIZE
    integrated = np.convolve(squared, window, mode='same')
    # Find peaks
    peaks, _ = sig.find_peaks(integrated, distance=SAMPLING_RATE//2)
    return peaks

def compute_rr_intervals(peak_indices):
    """Compute RR intervals in seconds."""
    intervals = np.diff(peak_indices) / SAMPLING_RATE
    return intervals

def classify_arrhythmia(rr_intervals):
    """Classify based on RR interval variability."""
    mean_rr = np.mean(rr_intervals)
    std_rr = np.std(rr_intervals)
    cv = std_rr / mean_rr
    
    # Detection threshold - this is the critical parameter
    if cv > threshold:
        return "ARRHYTHMIA"
    else:
        return "NORMAL"

def analyze_ecg(raw_signal):
    """Main analysis pipeline."""
    processed = preprocess_ecg(raw_signal)
    peaks = detect_qrs(processed)
    if len(peaks) < 2:
        return "INSUFFICIENT_DATA"
    rr = compute_rr_intervals(peaks)
    result = classify_arrhythmia(rr)
    return result

# Global threshold variable
threshold = 0.5  # default threshold

# Additional placeholder lines to reach line 85
# Line 51
# Line 52
# Line 53
# Line 54
# Line 55
# Line 56
# Line 57
# Line 58
# Line 59
# Line 60
# Line 61
# Line 62
# Line 63
# Line 64
# Line 65
# Line 66
# Line 67
# Line 68
# Line 69
# Line 70
# Line 71
# Line 72
# Line 73
# Line 74
# Line 75
# Line 76
# Line 77
# Line 78
# Line 79
# Line 80
# Line 81
# Line 82
# Line 83
# Line 84
# Line 85: threshold = 0.75  # new threshold proposed in PR #42