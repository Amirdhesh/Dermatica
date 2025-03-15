import joblib
import numpy as np
import cv2
from tensorflow.keras.applications.resnet50 import preprocess_input
from tensorflow.keras.models import load_model

le=joblib.load(r'D:\Dermatics\Dermatica\Backend\Model\label_encoder_resnet.pkl')
model = load_model(r'D:\Dermatics\Dermatica\Backend\Model\skinresnet.h5')

def model_prediction(img):
    try:
        skin_disease_categories = {
        "Psoriasis pictures Lichen Planus and related diseases": "Psoriasis",
        "Seborrheic Keratoses and other Benign Tumors": "Seborrheic Keratoses",
        "Tinea Ringworm Candidiasis and other Fungal Infections": "Tinea",
        "Acne and Rosacea Photos": "Acne",
        "Eczema Photos": "Eczema",
        "Actinic Keratosis Basal Cell Carcinoma and other Malignant Lesions": "Actinic Keratosis Basal Cell Carcinoma",
        "Warts Molluscum and other Viral Infections": "Warts Molluscum",
        "Nail Fungus and other Nail Disease": "Nail Fungus",
        "Systemic Disease": "Systemic Disease",
        "Light Diseases and Disorders of Pigmentation": "Light Diseases",
        "Atopic Dermatitis Photos": "Atopic Dermatitis",
        "Vascular Tumors": "Vascular Tumors",
        "Melanoma Skin Cancer Nevi and Moles": "Melanoma Skin Cancer Nevi",
        "Bullous Disease Photos": "Bullous Disease",
        "Scabies Lyme Disease and other Infestations and Bites": "Scabies Lyme Disease",
        "Lupus and other Connective Tissue diseases": "Lupus",
        "Vasculitis Photos": "Vasculitis",
        "Herpes HPV and other STDs Photos": "Herpes HPV",
        "Exanthems and Drug Eruptions": "Exanthems",
        "Cellulitis Impetigo and other Bacterial Infections": "Cellulitis Impetigo",
        "Poison Ivy Photos and other Contact Dermatitis": "Poison Ivy",
        "Hair Loss Photos Alopecia and other Hair Diseases": "Hair Loss",
        "Urticaria Hives": "Urticaria"
        }
        
        skin_disease_info = {
        "Psoriasis pictures Lichen Planus and related diseases": "Psoriasis is a chronic skin condition that speeds up the life cycle of skin cells, leading to a buildup of cells on the surface of the skin. Symptoms include red patches of skin, thick silvery scales, dry and cracked skin, and itching or burning. Causative agents include immune system dysfunction and genetic factors.",
        "Seborrheic Keratoses and other Benign Tumors": "Seborrheic Keratoses and other Benign Tumors is a non-cancerous skin growth that can appear anywhere on the skin surface. Symptoms include raised, waxy, scaly lesions that vary in color from white to black. They are generally painless and don't require treatment unless causing discomfort.",
        "Tinea Ringworm Candidiasis and other Fungal Infections": "Tinea Ringworm Candidiasis and other Fungal Infections refer to various fungal skin infections such as ringworm, candidiasis, etc. Symptoms include red, scaly rashes, itching, circular patches, raised borders, and sometimes blisters or pustules. Fungi like Trichophyton, Microsporum, and Epidermophyton cause these infections.",
        "Acne and Rosacea Photos": "Acne and Rosacea are skin conditions causing pimples, redness, and inflammation. Acne is often caused by clogged pores, excess oil production, and bacteria, resulting in whiteheads, blackheads, and cysts. Rosacea leads to facial redness and visible blood vessels due to unknown factors.",
        "Eczema Photos": "Eczema, or atopic dermatitis, is a chronic skin condition characterized by inflammation and itching. Symptoms include itching, red or brownish patches, dry skin, and cracked skin. Genetic and environmental factors contribute to its development.",
        "Actinic Keratosis Basal Cell Carcinoma and other Malignant Lesions": "Actinic Keratosis Basal Cell Carcinoma and other Malignant Lesions are skin conditions that may appear as rough, scaly patches (actinic keratosis) or as pearly or waxy bumps (basal cell carcinoma). They develop due to prolonged sun exposure and may require medical attention.",
        "Warts Molluscum and other Viral Infections": "Warts Molluscum and other Viral Infections are caused by viruses leading to skin growths like warts and molluscum contagiosum. Symptoms include raised, rough lesions with a grainy appearance (warts) or small, round bumps (molluscum contagiosum).",
        "Nail Fungus and other Nail Disease": "Nail Fungus and other Nail Disease involve fungal or bacterial infections affecting the nails. Symptoms include discoloration, thickening, or crumbling of nails, and sometimes pain or odor. These conditions often require treatment.",
        "Systemic Disease": "Systemic Disease refers to skin manifestations of internal health issues such as lupus, diabetes, or other systemic disorders. Symptoms vary widely and may include rashes, lesions, ulcers, or other skin changes indicating underlying health problems.",
        "Light Diseases and Disorders of Pigmentation": "Light Diseases and Disorders of Pigmentation include conditions affecting skin coloration such as albinism, melasma, or vitiligo. Symptoms include patches of lighter or darker skin color than the surrounding area due to genetic or environmental factors.",
        "Atopic Dermatitis Photos": "Atopic Dermatitis is a chronic skin condition that commonly begins in childhood and is often associated with other allergic conditions. Symptoms include itching, red to brownish patches, dry skin, and thickened skin. Genetic factors and immune system dysfunction are causative agents.",
        "Vascular Tumors": "Vascular Tumors are growths caused by abnormal blood vessels in the skin. These include conditions like hemangiomas and port-wine stains, appearing as red or purple marks on the skin.",
        "Melanoma Skin Cancer Nevi and Moles": "Melanoma Skin Cancer Nevi and Moles are skin cancer-related lesions. Melanoma is a dangerous form of skin cancer that can develop from existing moles or appear as new, suspicious lesions. Early detection is crucial.",
        "Bullous Disease Photos": "Bullous Disease refers to blistering skin conditions like pemphigus or bullous pemphigoid. Symptoms include large blisters on the skin or mucous membranes, which may itch or be painful.",
        "Scabies Lyme Disease and other Infestations and Bites": "Scabies Lyme Disease and other Infestations and Bites involve skin conditions caused by infestations like scabies or bites from insects or ticks. Symptoms include itching, rashes, and visible bite marks.",
        "Lupus and other Connective Tissue diseases": "Lupus and other Connective Tissue diseases encompass conditions affecting connective tissues like lupus erythematosus or scleroderma. Symptoms include rashes, joint pain, and skin thickening.",
        "Vasculitis Photos": "Vasculitis is inflammation of blood vessels causing redness, swelling, and sometimes ulceration or necrosis of the skin. Symptoms vary depending on the type of vasculitis and its severity.",
        "Herpes HPV and other STDs Photos": "Herpes HPV and other STDs Photos refer to sexually transmitted infections affecting the skin. Symptoms include genital warts, ulcers, or blisters in the genital or anal areas.",
        "Exanthems and Drug Eruptions": "Exanthems and Drug Eruptions are skin rashes caused by various factors such as medications, infections, or allergies. Symptoms include widespread rashes, itching, and sometimes blisters or peeling skin.",
        "Cellulitis Impetigo and other Bacterial Infections": "Cellulitis Impetigo and other Bacterial Infections are skin infections caused by bacteria like Staphylococcus or Streptococcus. Symptoms include redness, swelling, and sometimes fluid-filled blisters or sores.",
        "Poison Ivy Photos and other Contact Dermatitis": "Poison Ivy Photos and other Contact Dermatitis include skin reactions triggered by contact with irritants or allergens like poison ivy, causing itching, redness, and sometimes blisters or oozing.",
        "Hair Loss Photos Alopecia and other Hair Diseases": "Hair Loss Photos Alopecia and other Hair Diseases encompass conditions causing hair loss like alopecia areata or male/female pattern baldness. Symptoms include thinning or loss of hair in patches or overall.",
        "Urticaria Hives": "Urticaria, commonly known as hives, is a skin reaction characterized by raised, itchy welts appearing on the skin due to allergies, medications, or other triggers."
        }


        classes = ['Acne and Rosacea Photos',
        'Actinic Keratosis Basal Cell Carcinoma and other Malignant Lesions',
        'Atopic Dermatitis Photos', 'Bullous Disease Photos',
        'Cellulitis Impetigo and other Bacterial Infections',
        'Eczema Photos', 'Exanthems and Drug Eruptions',
        'Hair Loss Photos Alopecia and other Hair Diseases',
        'Herpes HPV and other STDs Photos',
        'Light Diseases and Disorders of Pigmentation',
        'Lupus and other Connective Tissue diseases',
        'Melanoma Skin Cancer Nevi and Moles',
        'Nail Fungus and other Nail Disease',
        'Poison Ivy Photos and other Contact Dermatitis',
        'Psoriasis pictures Lichen Planus and related diseases',
        'Scabies Lyme Disease and other Infestations and Bites',
        'Seborrheic Keratoses and other Benign Tumors', 'Systemic Disease',
        'Tinea Ringworm Candidiasis and other Fungal Infections',
        'Urticaria Hives', 'Vascular Tumors', 'Vasculitis Photos',
        'Warts Molluscum and other Viral Infections']

        # Resize and preprocess the image
        img = cv2.resize(img, (224,224))
        img = preprocess_input(np.array([img]))

        # Predict the class
        predictions = model.predict(img)
        predicted_class_index = np.argmax(predictions)
        output = le.classes_[predicted_class_index]
        confidence = max(predictions[0])

        # Get disease and comment
        disease = skin_disease_categories[output]
        comment = skin_disease_info[output]
        return {"success":True,"disease":disease,"comment":comment,"confidence":f'{str(round(confidence*100,2))}%'}
    except Exception as e :
        return {"success":False}
        