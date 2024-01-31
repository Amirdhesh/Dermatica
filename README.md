# Dermatica


Dermatica is a web application designed for the accurate identification of dermatological diseases. Utilizing an advanced deep learning model, Dermatica excels in classifying skin conditions across 23 different classes. Whether you're a healthcare professional or an individual concerned about skin health, Dermatica provides an intuitive and efficient platform for obtaining insights into various skin abnormalities. It is particularly useful for preliminary diagnosis.

Dermatica is equipped to identify various dermatological conditions across 23 different classes. These classes include:

1. Acne and Rosacea Photos
2. Actinic Keratosis Basal Cell Carcinoma and other Malignant Lesions
3. Atopic Dermatitis Photos
4. Bullous Disease Photos
5. Cellulitis Impetigo and other Bacterial Infections
6. Eczema Photos
7. Exanthems and Drug Eruptions
8. Hair Loss Photos Alopecia and other Hair Diseases
9. Herpes HPV and other STDs Photos
10. Light Diseases and Disorders of Pigmentation
11. Lupus and other Connective Tissue diseases
12. Melanoma Skin Cancer Nevi and Moles
13. Nail Fungus and other Nail Disease
14. Poison Ivy Photos and other Contact Dermatitis
15. Psoriasis pictures Lichen Planus and related diseases
16. Scabies Lyme Disease and other Infestations and Bites
17. Seborrheic Keratoses and other Benign Tumors
18. Systemic Disease
19. Tinea Ringworm Candidiasis and other Fungal Infections
20. Urticaria Hives
21. Vascular Tumors
22. Vasculitis Photos
23. Warts Molluscum and other Viral Infections

Explore the comprehensive list of skin condition classes that Dermatica can accurately classify. Understanding these classes allows you to gain valuable insights into a diverse range of skin abnormalities.

## How to Use 👇

1. Clone the repository:
    ~~~
    bash
    git clone https://github.com/ramakrishnan2503/Dermatica.git
    ~~~   

2. Install the required dependencies:
    ~~~
    bash
    pip install -r Requirements.txt
    ~~~ 

3. Run the app:
    ~~~
    bash
    python app.py
    ~~~

4. Open your web browser and navigate to:
   ~~~
   localhost:5000
   ~~~
6. Upload an image of a skin condition to get predictions.

## Model Details

Dermatica leverages a pre-trained ResNet model for the identification of dermatological diseases. This model, built with TensorFlow, is specifically tailored for processing dermatological images and making accurate predictions based on the learned patterns.

## Dataset
The model was trained on a diverse dataset available at Dermnet Dataset on Kaggle. This dataset encompasses various skin conditions, enabling the model to generalize well across different disease categories.

## Model Architecture
The underlying architecture utilizes ResNet50, a powerful deep learning model known for its ability to capture intricate features in images. Additional layers, including Global Average Pooling and Dense layers, were added to facilitate the classification of skin conditions.

## File Structure
~~~
- Dermatica/
   |
   |_ Backend/
        |
        |─ Model/
        |  |
        |  |─ _init_.py
        |  |_ model.py
        |
        |─ Templete/
        |  |
        |  |─ base.html
        |  |_ home.html
        |
        |─ Test/
        |  |
        |  |─ _init_.py
        |  |_ test_dermatica.py
        |
        |─ .gitignore
        |─.pre-commit-config.yaml
        |─ app.py
        |_ Requirement.txt
~~~
## Acknowledgments

- The ResNet model used in this app was trained on a dataset to enable accurate identification of various skin conditions.

    *Dataset Link*: [Dermnet - Kaggle](https://www.kaggle.com/datasets/shubhamgoel27/dermnet)
