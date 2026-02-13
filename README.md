### Building Function Classification using Metadata

This repository implements a machine learning pipeline to classify building footprints as Residential, Non-Residential or Industrial for Indian and Kenyan environments. 

The [first version of the model](https://github.com/Open-Building-Insights/classification-model) attempted to classify the buildings using satellite imagery, however it faced different challenges. It became a processing bottleneck and resource consuming with low resolution (10m), lacking training data to successfully classify households, above all in rural environments. This new model utilizes numeric metadata derived from building geometries and OpenStreetMap (OSM) context for the training purposes, and synthetic generated data where data is not enough. 

- **Model Architecture:** Deep Neural  Network (10 inputs -> Hidden Layers -> 3 Output Buckets).

- **Input Layer:** Matches the feature set (10 numeric inputs).
- **Hidden Layers:**
  - Dense (100 neurons, ReLU) + Dropout (20%)
  - Dense (100 neurons, ReLU) + Dropout (20%)
  - Dense (64 neurons, ReLU) + Dropout (10%)
  - Dense (32 neurons, ReLU) + Dropout (10%)
  - Dense (16 neurons, ReLU) -> Dense (8) -> Dense (4).
- **Output Layer:** Dense (3 neurons, Softmax) for the 3 classes: Non-Residential, Residential, Industrial.
Optimizer: Adam with a learning rate of 0.001.

### Methodology
The model discards pixel-based analysis in favor of 10 numeric attributes categorized into two types:

- **Inherent Attributes (Building Morphology):**
  - **1. Area:** Footprint size.
  - **2. Squareness:** Perimeter compared to a perfect square of the same area.
  - **3. Faces:** Number of distinct walls/sides.

- **Contextual Attributes (Urban Fabric):** 
  - **4 Building Density:** Count within a 100m buffer.
  - **5. 6. 7. 8. Proximity:** Road network is extracted from OSM and distances are computed based on the following classification:
    - Distance to 1: motorway, trunk link, motorway link, trunk, primary, primary link
    - Distance to 2: secondary, secondary link
    - Distance to 3: tertiary, tertiary link
    - Distance to 4: residential, footway, service, unclassified, living street, steps, path, track, pedestrian, cycleway, raceway, bridleway, construction service, bus stop, rest area, yes, emergency access point, corridor, junction, proposed, minor.
  - **9. 10 Road Density:** Density within a 200m and 100m buffer for Distance to 4 roads.

- **Performance:** 
~72% Accuracy against Ground Truth (MHD).
~80% Accuracy against OSM Test Set.



