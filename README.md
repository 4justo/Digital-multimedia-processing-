# CCS3208 Week 2 Lab

Python exercises for the Multimedia Systems Week 2 laboratory. The work covers
sampled audio, image point and neighbourhood processing, basic video processing,
and simple audio synthesis. `Lab_report.docx` contains the accompanying report.

## Requirements

- Python 3.9 or later
- Packages in `requirements.txt`

Create an isolated environment and install the dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate          # Windows: .venv\\Scripts\\activate
python3 -m pip install -r requirements.txt
```

## Running the exercises

Run scripts from the repository root so relative media paths resolve correctly:

```bash
python3 partA.py
python3 partc4.py
python3 partE1.py
```

Most scripts display plots in Matplotlib windows. Close each window to let the
script continue. Video exercises require `input.mp4`; image exercises require
`image.jpg` (despite its extension, this supplied file is PNG-formatted).

## Exercise guide

| Area | Scripts | What they demonstrate |
| --- | --- | --- |
| Audio sampling | `partA.py`, `partB.py` | Generating and inspecting sine waves at different frequencies and amplitudes |
| Image point processing | `partc1.py`–`partc4.py` | Loading an image, brightness adjustment, negatives, grayscale conversion, and thresholding |
| Image neighbourhood processing | `partD2.py`, `partD3.py` | Mean filtering and sharpening with OpenCV |
| Video processing | `partE1.py`–`partE3.py` | Inspecting video metadata, extracting grayscale frames, and resizing a frame |
| Audio synthesis | `partF1.py`, `partF2.py`, `partf3.py` | Waveform comparison, additive synthesis, and an ADSR-style envelope |

`partE2.py` writes up to five files named `gray_frame_0.jpg` through
`gray_frame_4.jpg`. `partE3.py` writes `resized_frame.jpg`; rerunning either
script replaces its corresponding output files.

## Notes

- Filenames retain the original lab naming/capitalization (`partc*.py` and
  `partf3.py`), so use the names exactly as shown.
- The supplied media and example output images are intentionally tracked; only
  local Python environments, caches, and editor metadata are ignored.
