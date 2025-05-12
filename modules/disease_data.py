class Disease:
    def __init__(self, name, symptoms, medication, precautions, tips):
        self.name = name
        self.symptoms = symptoms
        self.medication = medication
        self.precautions = precautions
        self.tips = tips

    def matches(self, user_input):
        user_input_lower = user_input.lower()
        if self.name.lower() in user_input_lower:
            return True
        return any(symptom.lower() in user_input_lower for symptom in self.symptoms)
# diseases names, symptoms, medication, precautions and tips
DISEASES = [
    Disease(
        name="Flu",
        symptoms=["fever", "cough", "sore throat", "fatigue", "body aches"],
        medication="Paracetamol, Ibuprofen",
        precautions="Rest, stay hydrated, avoid cold environments",
        tips="Drink warm fluids, use humidifier, get enough sleep"
    ),
    Disease(
        name="Diabetes",
        symptoms=["frequent urination", "excessive thirst", "fatigue", "blurred vision"],
        medication="Insulin, Metformin",
        precautions="Monitor blood sugar, regular exercise, avoid sugar",
        tips="Eat balanced meals, stay active, check blood sugar regularly"
    ),
    Disease(
        name="Flu",
        symptoms=["fever", "chills", "muscle aches", "sore throat", "runny nose", "vomiting", "body pain"],
        medication="Paracetamol, Fluids, Rest",
        precautions="Avoid cold drinks, wear warm clothes, isolate from others",
        tips="Drink ginger tea, gargle with warm salt water, take steam"
    ),
    Disease(
        name="Migraine",
        symptoms=["headache", "nausea", "sensitivity to light", "blurred vision"],
        medication="Pain relievers, Triptans, Anti-nausea meds",
        precautions="Avoid stress, caffeine, and screen exposure",
        tips="Use cold compress, rest in a dark room"
    ),
    Disease(
        name="Food Poisoning",
        symptoms=["vomiting", "diarrhea", "abdominal pain", "nausea"],
        medication="ORS, antiemetics, activated charcoal",
        precautions="Avoid street food, wash hands, drink bottled water",
        tips="Eat bland foods like bananas, rice, applesauce"
    ),
    Disease(
    name="Flu",
    symptoms=["fever", "chills", "headache", "body aches", "cough", "fatigue"],
    medication="Antiviral drugs like oseltamivir (Tamiflu), Paracetamol for fever",
    precautions="Wash your hands regularly, Avoid close contact with sick individuals",
    tips="Rest, hydrate, and use over-the-counter medications for symptom relief"
),
Disease(
    name="Cold",
    symptoms=["runny nose", "sore throat", "cough", "congestion", "mild fatigue"],
    medication="Decongestants, Antihistamines, Paracetamol for fever",
    precautions="Avoid touching your face, Cover your coughs, Drink plenty of fluids",
    tips="Use saline nasal spray, Rest, Avoid smoke and allergens"
),
Disease(
    name="Stomach Flu",
    symptoms=["nausea", "vomiting", "diarrhea", "stomach cramps", "fever"],
    medication="ORS (Oral Rehydration Solution), Anti-nausea medication",
    precautions="Wash your hands frequently, Stay hydrated",
    tips="Eat bland foods, Avoid dairy and spicy foods, Drink fluids regularly"
),
Disease(
    name="Migraine",
    symptoms=["severe headache", "nausea", "vomiting", "sensitivity to light and sound"],
    medication="Triptans, Pain relievers like ibuprofen, Antiemetics",
    precautions="Rest in a dark room, Avoid triggers like bright lights",
    tips="Apply a cold compress, Relaxation techniques, Stay hydrated"
),
Disease(
    name="Anxiety",
    symptoms=["nervousness", "rapid heartbeat", "shortness of breath", "restlessness"],
    medication="Antidepressants, Benzodiazepines",
    precautions="Avoid caffeine, Practice mindfulness and deep breathing",
    tips="Exercise regularly, Seek support from a therapist"
),
Disease(
    name="Food Poisoning",
    symptoms=["vomiting", "diarrhea", "abdominal pain", "nausea"],
    medication="ORS, antiemetics, activated charcoal",
    precautions="Avoid street food, wash hands, drink bottled water",
    tips="Eat bland foods like bananas, rice, applesauce"
),
Disease(
    name="Chickenpox",
    symptoms=["red spots", "itchy rash", "fever", "tiredness"],
    medication="Antihistamines, Calamine lotion for itching",
    precautions="Avoid contact with others, Isolate until all spots scab over",
    tips="Cool baths, Use moisturizing creams, Stay hydrated"
),
Disease(
    name="Pneumonia",
    symptoms=["cough", "chest pain", "fever", "shortness of breath", "fatigue"],
    medication="Antibiotics (bacterial pneumonia), Antiviral drugs (viral pneumonia)",
    precautions="Vaccination, Avoid smoking, Stay away from sick people",
    tips="Get plenty of rest, Drink fluids, Use a humidifier"
),
Disease(
    name="Asthma",
    symptoms=["wheezing", "shortness of breath", "coughing", "chest tightness"],
    medication="Inhalers (Bronchodilators), Steroids",
    precautions="Avoid asthma triggers, Maintain a clean environment",
    tips="Carry a rescue inhaler, Monitor your symptoms, Use a peak flow meter"
),
Disease(
    name="Diabetes",
    symptoms=["frequent urination", "extreme thirst", "fatigue", "blurry vision"],
    medication="Insulin, Oral medications like metformin",
    precautions="Monitor blood sugar regularly, Maintain a healthy diet",
    tips="Exercise regularly, Manage stress, Avoid sugary foods"
),
Disease(
    name="Hypertension",
    symptoms=["headache", "dizziness", "shortness of breath", "nosebleeds"],
    medication="ACE inhibitors, Diuretics, Calcium channel blockers",
    precautions="Reduce salt intake, Regularly monitor blood pressure",
    tips="Exercise regularly, Manage stress, Limit alcohol intake"
),
Disease(
    name="Tuberculosis",
    symptoms=["persistent cough", "fever", "night sweats", "weight loss"],
    medication="Antibiotics (Rifampicin, Isoniazid)",
    precautions="Wear a mask, Stay away from others until you're no longer contagious",
    tips="Follow the treatment plan strictly, Stay hydrated"
),
Disease(
    name="HIV/AIDS",
    symptoms=["fatigue", "weight loss", "frequent infections", "swollen lymph nodes"],
    medication="Antiretroviral therapy (ART)",
    precautions="Safe sex practices, Regular HIV testing",
    tips="Take your medication regularly, Maintain a healthy diet"
),
Disease(
    name="Hepatitis",
    symptoms=["yellowing of the skin", "fatigue", "abdominal pain", "loss of appetite"],
    medication="Antiviral medications (for hepatitis B and C)",
    precautions="Avoid sharing needles, Practice safe sex",
    tips="Drink plenty of fluids, Avoid alcohol, Eat small, frequent meals"
),
Disease(
    name="Malaria",
    symptoms=["fever", "chills", "headache", "sweating", "fatigue"],
    medication="Antimalarial drugs (Chloroquine, Artemisinin-based combination therapy)",
    precautions="Use insect repellent, Sleep under mosquito nets",
    tips="Stay hydrated, Take prescribed medications, Rest"
),
Disease(
    name="Shingles",
    symptoms=["painful rash", "blisters", "fever", "headache"],
    medication="Antiviral medications (Acyclovir)",
    precautions="Avoid contact with vulnerable individuals, Use cool compresses",
    tips="Keep the rash clean and dry, Take pain relievers"
),
Disease(
    name="Sore Throat",
    symptoms=["sore throat", "pain while swallowing", "red throat"],
    medication="Pain relievers like paracetamol, Lozenges",
    precautions="Avoid smoking, Stay hydrated, Rest",
    tips="Gargle warm salt water, Avoid irritants like strong fumes"
),
Disease(
    name="Conjunctivitis (Pink Eye)",
    symptoms=["redness in the eye", "itchiness", "watery eyes"],
    medication="Antihistamines, Antibiotic eye drops (for bacterial infections)",
    precautions="Wash your hands frequently, Avoid touching your eyes",
    tips="Use cool compresses, Avoid wearing makeup"
),
Disease(
    name="Psoriasis",
    symptoms=["red, scaly patches on skin", "itching", "dry skin"],
    medication="Topical creams, Phototherapy, Biologics",
    precautions="Avoid triggers like stress, hot water",
    tips="Moisturize regularly, Avoid scratching, Practice relaxation techniques"
),
Disease(
    name="Eczema",
    symptoms=["itchy skin", "red rashes", "dry skin", "blisters"],
    medication="Topical steroids, Antihistamines for itching",
    precautions="Avoid triggers like harsh soaps, Use gentle skin products",
    tips="Keep skin moisturized, Avoid scratching, Use lukewarm water for baths"
),
Disease(
    name="Acne",
    symptoms=["pimples", "blackheads", "whiteheads", "cystic lumps on the skin"],
    medication="Topical treatments (benzoyl peroxide, salicylic acid), Oral antibiotics",
    precautions="Avoid touching your face, Use non-comedogenic products",
    tips="Cleanse your skin twice a day, Use oil-free moisturizers"
),
Disease(
    name="Arthritis",
    symptoms=["joint pain", "swelling", "stiffness", "reduced range of motion"],
    medication="Pain relievers, NSAIDs, Disease-modifying antirheumatic drugs (DMARDs)",
    precautions="Avoid overexertion, Maintain a healthy weight",
    tips="Exercise regularly, Use assistive devices for joints, Apply heat/cold packs"
),
Disease(
    name="Gallstones",
    symptoms=["severe abdominal pain", "nausea", "vomiting", "indigestion"],
    medication="Pain relievers, Ursodeoxycholic acid",
    precautions="Avoid high-fat meals, Maintain a healthy weight",
    tips="Eat smaller, more frequent meals, Drink plenty of water"
),
Disease(
    name="Gastritis",
    symptoms=["abdominal pain", "nausea", "vomiting", "loss of appetite"],
    medication="Antacids, Proton pump inhibitors, Antibiotics (if H. pylori infection is present)",
    precautions="Avoid spicy and acidic foods, Limit alcohol consumption",
    tips="Eat smaller meals, Avoid smoking, Drink plenty of water"
),
Disease(
    name="Osteoporosis",
    symptoms=["bone pain", "fractures", "loss of height", "stooped posture"],
    medication="Bisphosphonates, Calcium and vitamin D supplements",
    precautions="Avoid smoking, Engage in weight-bearing exercises",
    tips="Eat calcium-rich foods, Maintain a healthy weight, Limit alcohol intake"
),
Disease(
    name="Sinusitis",
    symptoms=["nasal congestion", "facial pain", "headache", "fever"],
    medication="Decongestants, Nasal steroids, Antibiotics (if bacterial)",
    precautions="Avoid allergens, Use a humidifier",
    tips="Use saline nasal spray, Drink plenty of fluids, Rest"
),
Disease(
    name="Tonsillitis",
    symptoms=["sore throat", "fever", "swollen tonsils", "difficulty swallowing"],
    medication="Antibiotics (if bacterial), Pain relievers",
    precautions="Rest, Stay hydrated, Avoid contact with others",
    tips="Gargle salt water, Use throat lozenges, Warm drinks"
),
Disease(
    name="Urinary Tract Infection (UTI)",
    symptoms=["frequent urination", "burning sensation while urinating", "cloudy urine", "lower abdominal pain"],
    medication="Antibiotics, Pain relievers (like phenazopyridine)",
    precautions="Wipe front to back, Drink plenty of water, Avoid holding urine",
    tips="Urinate after sexual activity, Avoid irritants like bubble baths"
),
Disease(
    name="Vertigo",
    symptoms=["dizziness", "spinning sensation", "nausea", "loss of balance"],
    medication="Antihistamines, Anticholinergics",
    precautions="Avoid sudden head movements, Rest in a dark room",
    tips="Perform balance exercises, Avoid triggers like bright lights"
),
Disease(
    name="Chronic Fatigue Syndrome",
    symptoms=["extreme tiredness", "muscle pain", "headache", "sleep disturbances"],
    medication="Pain relievers, Antidepressants, Sleep aids",
    precautions="Avoid overexertion, Maintain a consistent sleep schedule",
    tips="Rest regularly, Pace activities, Eat a balanced diet"
),
Disease(
    name="Dengue Fever",
    symptoms=["high fever", "rash", "muscle and joint pain", "headache"],
    medication="Pain relievers (Paracetamol), IV fluids (if severe)",
    precautions="Avoid mosquito bites, Stay in mosquito-protected areas",
    tips="Stay hydrated, Rest, Avoid aspirin and NSAIDs"
),
Disease(
    name="Ebola",
    symptoms=["fever", "fatigue", "muscle pain", "vomiting", "diarrhea", "bleeding"],
    medication="Supportive care, Antiviral medications (in some cases)",
    precautions="Avoid contact with infected individuals, Use protective equipment",
    tips="Practice good hygiene, Avoid touching eyes, nose, or mouth"
),
Disease(
    name="Liver Cirrhosis",
    symptoms=["fatigue", "nausea", "abdominal pain", "yellowing of the skin", "swelling in the legs"],
    medication="Antiviral drugs (for hepatitis-related cirrhosis), Diuretics for fluid retention",
    precautions="Avoid alcohol, Maintain a low-salt diet",
    tips="Stay hydrated, Eat small meals frequently, Avoid liver-toxic medications"
),
Disease(
    name="Multiple Sclerosis",
    symptoms=["numbness", "vision problems", "balance problems", "muscle weakness"],
    medication="Disease-modifying therapies (interferons), Corticosteroids for flare-ups",
    precautions="Avoid overheating, Exercise regularly",
    tips="Take breaks, Use assistive devices if needed, Manage stress"
),
Disease(
    name="Parkinson's Disease",
    symptoms=["tremors", "stiffness", "slowness of movement", "balance problems"],
    medication="Levodopa, Dopamine agonists, Anticholinergic drugs",
    precautions="Avoid falls, Maintain a regular exercise routine",
    tips="Use physical therapy, Stay active, Eat a balanced diet"
),
Disease(
    name="Sickle Cell Anemia",
    symptoms=["fatigue", "pain episodes", "shortness of breath", "swelling in the hands and feet"],
    medication="Pain relievers, Hydroxyurea, Blood transfusions",
    precautions="Avoid extreme temperatures, Stay hydrated",
    tips="Rest during pain episodes, Follow a healthy diet, Manage stress"
),
Disease(
    name="Hearing Loss",
    symptoms=["difficulty hearing", "muffled sounds", "ringing in ears (tinnitus)"],
    medication="Hearing aids, Cochlear implants (for severe loss)",
    precautions="Avoid prolonged exposure to loud noise, Use ear protection",
    tips="Get regular hearing tests, Reduce noise exposure, Maintain good ear hygiene"
),
Disease(
    name="Hemorrhoids",
    symptoms=["rectal pain", "itching", "bleeding during bowel movements", "swelling around the anus"],
    medication="Topical creams, Sitz baths, Stool softeners",
    precautions="Avoid straining, Eat a high-fiber diet",
    tips="Use ice packs, Take warm baths, Exercise regularly"
),
Disease(
    name="Shigellosis",
    symptoms=["diarrhea (often bloody)", "abdominal cramps", "fever", "nausea"],
    medication="Antibiotics (for severe cases), ORS (Oral Rehydration Solution)",
    precautions="Wash hands frequently, Avoid contaminated food and water",
    tips="Eat bland foods, Drink plenty of fluids, Avoid dairy products"
),
Disease(
    name="Pregnancy (Normal)",
    symptoms=["morning sickness", "fatigue", "breast tenderness", "increased urination"],
    medication="Prenatal vitamins, Folate supplements",
    precautions="Avoid smoking, Limit caffeine intake, Maintain a healthy diet",
    tips="Stay hydrated, Get plenty of rest, Do light exercises like walking"
),
Disease(
    name="Morning Sickness (Pregnancy)",
    symptoms=["nausea", "vomiting", "fatigue", "food aversions"],
    medication="Vitamin B6, Antihistamines, Ginger supplements",
    precautions="Avoid strong smells, Eat small frequent meals, Stay hydrated",
    tips="Drink ginger tea, Avoid spicy or greasy foods, Take naps during the day"
),
Disease(
    name="Gestational Diabetes",
    symptoms=["increased thirst", "frequent urination", "fatigue", "blurred vision"],
    medication="Insulin, Metformin (if required)",
    precautions="Monitor blood sugar levels regularly, Eat a balanced diet",
    tips="Exercise regularly, Eat smaller, balanced meals, Avoid sugary foods"
),
Disease(
    name="Preeclampsia",
    symptoms=["high blood pressure", "swelling in the hands and feet", "protein in urine"],
    medication="Antihypertensive drugs, Magnesium sulfate (for seizures)",
    precautions="Regular prenatal checkups, Monitor blood pressure",
    tips="Rest regularly, Stay hydrated, Avoid salty foods"
),
Disease(
    name="Ectopic Pregnancy",
    symptoms=["abdominal pain", "vaginal bleeding", "shoulder pain", "dizziness"],
    medication="Surgical removal of the pregnancy, Methotrexate injection (if early)",
    precautions="Early prenatal care, Monitor any abnormal symptoms",
    tips="Seek immediate medical attention if symptoms appear, Get regular scans"
),
Disease(
    name="Urinary Tract Infection (UTI) in Pregnancy",
    symptoms=["painful urination", "frequent urination", "lower abdominal pain"],
    medication="Antibiotics (safe for pregnancy)",
    precautions="Drink plenty of water, Wipe front to back",
    tips="Avoid holding in urine, Drink cranberry juice, Urinate after sex"
),
Disease(
    name="Thyroid Disorders (Pregnancy)",
    symptoms=["fatigue", "weight gain or loss", "swelling in the neck", "feeling cold or hot"],
    medication="Levothyroxine (for hypothyroidism), Antithyroid drugs (for hyperthyroidism)",
    precautions="Regular thyroid function tests, Take medication as prescribed",
    tips="Eat a balanced diet, Stay active, Get enough rest"
),
Disease(
    name="Postpartum Depression",
    symptoms=["feelings of sadness", "fatigue", "loss of interest in activities", "changes in appetite"],
    medication="Antidepressants, Therapy (Cognitive Behavioral Therapy)",
    precautions="Seek support from family and friends, Avoid isolation",
    tips="Take time for self-care, Reach out to a mental health professional, Get regular sleep"
),
Disease(
    name="Acid Reflux (GERD)",
    symptoms=["heartburn", "acidic taste in the mouth", "regurgitation", "difficulty swallowing"],
    medication="Antacids, Proton pump inhibitors, H2 blockers",
    precautions="Avoid spicy and fatty foods, Eat smaller meals",
    tips="Eat slowly, Avoid lying down right after meals, Raise the head of the bed"
),
Disease(
    name="Asthma",
    symptoms=["wheezing", "shortness of breath", "coughing", "tightness in the chest"],
    medication="Inhalers (bronchodilators, corticosteroids), Leukotriene modifiers",
    precautions="Avoid asthma triggers, Use a peak flow meter",
    tips="Monitor lung function, Exercise with caution, Avoid smoke and dust"
),
Disease(
    name="Bronchitis",
    symptoms=["persistent cough", "mucus production", "shortness of breath", "fatigue"],
    medication="Cough suppressants, Bronchodilators, Antibiotics (if bacterial)",
    precautions="Avoid smoke, Stay hydrated",
    tips="Rest frequently, Use a humidifier, Drink warm liquids"
),
Disease(
    name="Chronic Sinusitis",
    symptoms=["nasal congestion", "facial pain", "headache", "coughing"],
    medication="Decongestants, Nasal corticosteroids, Antibiotics (if bacterial)",
    precautions="Avoid allergens, Use a humidifier",
    tips="Use saline nasal spray, Drink plenty of fluids, Rest"
),
Disease(
    name="Celiac Disease",
    symptoms=["diarrhea", "bloating", "fatigue", "weight loss", "anemia"],
    medication="Gluten-free diet",
    precautions="Avoid gluten-containing foods",
    tips="Read labels carefully, Substitute gluten-free grains, Seek a nutritionist"
),
Disease(
    name="Diabetes Type 1",
    symptoms=["increased thirst", "frequent urination", "extreme hunger", "fatigue"],
    medication="Insulin injections, Insulin pumps",
    precautions="Monitor blood sugar levels, Eat a balanced diet",
    tips="Exercise regularly, Maintain a healthy weight, Stay hydrated"
),
Disease(
    name="Diabetes Type 2",
    symptoms=["increased thirst", "frequent urination", "blurry vision", "tiredness"],
    medication="Metformin, Insulin (if required)",
    precautions="Monitor blood sugar, Avoid processed sugars",
    tips="Exercise regularly, Eat healthy foods, Lose weight if necessary"
),
Disease(
    name="Hypertension (High Blood Pressure)",
    symptoms=["headaches", "shortness of breath", "nosebleeds", "dizziness"],
    medication="Diuretics, ACE inhibitors, Beta-blockers",
    precautions="Reduce salt intake, Monitor blood pressure regularly",
    tips="Exercise regularly, Reduce alcohol intake, Avoid stress"
),
Disease(
    name="Influenza (Flu)",
    symptoms=["fever", "chills", "muscle aches", "fatigue", "cough"],
    medication="Antiviral drugs (Oseltamivir), Pain relievers",
    precautions="Get vaccinated, Wash hands frequently",
    tips="Rest, Drink fluids, Avoid close contact with others"
),
Disease(
    name="Irritable Bowel Syndrome (IBS)",
    symptoms=["abdominal pain", "bloating", "diarrhea", "constipation"],
    medication="Antispasmodics, Laxatives, Antidiarrheal medications",
    precautions="Avoid trigger foods (like dairy, fatty foods)",
    tips="Eat small meals, Stay hydrated, Manage stress"
),
Disease(
    name="Lung Cancer",
    symptoms=["persistent cough", "weight loss", "shortness of breath", "chest pain"],
    medication="Chemotherapy, Radiation therapy, Immunotherapy",
    precautions="Avoid smoking, Stay away from secondhand smoke",
    tips="Exercise regularly, Maintain a healthy weight, Eat a balanced diet"
),
Disease(
    name="Lupus",
    symptoms=["fatigue", "joint pain", "skin rashes", "fever"],
    medication="NSAIDs, Corticosteroids, Immunosuppressive drugs",
    precautions="Avoid sunlight, Regular checkups",
    tips="Get plenty of rest, Stay active, Avoid stress"
), 
Disease(
    name="Normal Menstrual Cramps (Primary Dysmenorrhea)",
    symptoms=["mild to moderate lower abdominal pain", "cramping", "back pain"],
    medication="NSAIDs (Ibuprofen, Naproxen), Heating pads, Mild pain relievers",
    precautions="Stay hydrated, Avoid caffeine, Avoid stress",
    tips="Use heating pads, Practice relaxation techniques like yoga or meditation"
),
Disease(
    name="Heavy Menstrual Bleeding (Menorrhagia)",
    symptoms=["excessive menstrual bleeding", "passing large clots", "fatigue", "anemia"],
    medication="Tranexamic acid, Birth control pills, Hormonal treatments",
    precautions="Use menstrual cups or thicker pads, Regularly monitor blood loss",
    tips="Stay hydrated, Eat iron-rich foods to prevent anemia, Take breaks during physical activities"
),
Disease(
    name="Irregular Periods (Oligomenorrhea)",
    symptoms=["periods that come less frequently", "long intervals between periods"],
    medication="Birth control pills, Hormonal therapies",
    precautions="Maintain a balanced lifestyle, Regular exercise",
    tips="Track your menstrual cycle, Avoid stress, Maintain a healthy diet"
),
Disease(
    name="Light Menstrual Bleeding (Hypomenorrhea)",
    symptoms=["very light or scanty periods", "short duration of menstruation"],
    medication="Birth control pills, Hormonal therapy",
    precautions="Monitor the cycle, Maintain a balanced diet",
    tips="Keep track of your cycle, Ensure adequate nutrition, Manage stress"
),
Disease(
    name="Premenstrual Syndrome (PMS)",
    symptoms=["mood swings", "bloating", "breast tenderness", "fatigue", "irritability"],
    medication="NSAIDs, Birth control pills, Antidepressants",
    precautions="Avoid alcohol and caffeine, Eat small meals regularly, Get enough sleep",
    tips="Practice relaxation techniques, Exercise regularly, Avoid stress"
),
]
