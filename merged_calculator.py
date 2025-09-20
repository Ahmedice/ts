import streamlit as st
import pandas as pd

# --- Language Dictionary ---
MESSAGES = {
    "en": {
        "title": "🧫 Tissue Culture Calculator",
        "intro": "Tool for calculating cell culture (Primary culture & Passage)",
        "general_settings": "General Settings",
        "experiment_type": "Select Experiment Type:",
        "primary_culture": "Primary Culture",
        "passage": "Passage",
        "cell_line_selection": "Cell Line Selection",
        "select_cell_line": "Select Cell Line:",
        "custom": "Custom",
        "new_cell_line_name": "New Cell Line Name:",
        "cell_type": "Cell Type:",
        "adherent_cm2": "Adherent (per cm²)",
        "suspension_ml": "Suspension (per ml)",
        "seeding_density": "Enter Seeding Density:",
        "add_new_cell_line": "➕ Add New Cell Line",
        "add_success": "{} added successfully!",
        "add_error": "Please enter a valid name and density for the cell line.",
        "use_custom_seeding_density": "Use custom seeding density?",
        "custom_seeding_density_input": "Enter Custom Seeding Density (cells/cm² or cells/ml):",
        "flask_settings": "Flask Settings",
        "select_flask": "Select Flask:",
        "num_units": "Number of Units (Flasks/Plates):",
        "initial_cell_concentration": "Initial Cell Suspension Concentration (cells/ml):",
        "split_ratio": "Split ratio (e.g., 1:3)",
        "split_ratio_error": "Incorrect Split ratio format. Use 1:N",
        "total_medium_per_flask": "Total Medium Volume per {} (ml):",
        "medium_components": "Medium Components",
        "base_medium_name": "Base Medium Name:",
        "serum_percent": "Serum %:",
        "antibiotic_percent": "Antibiotic %:",
        "supplements_percent": "Other Supplements %:",
        "detailed_results": "📊 Detailed Results",
        "cell_calculation": "1️⃣ Cell Calculation",
        "total_cells_needed": "Total Cells Required (for seeding)",
        "equation": "Equation",
        "result": "Result",
        "practical_execution": "Practical Execution",
        "cells_per_flask_after_split": "Cells per flask after Split Ratio (if {})",
        "volume_needed_for_cells": "Volume of Cell Suspension Needed to Reach {:,} cells",
        "draw_ul_from_suspension": "Draw {:,} µl from cell suspension",
        "total_medium_preparation": "2️⃣ Total Medium Preparation",
        "component": "Component",
        "percentage": "Percentage",
        "calculation": "Calculation",
        "final_volume": "Final Volume",
        "add_ml": "Add {:.2f} ml",
        "prepare_single_flask": "3️⃣ Prepare Each {} Separately",
        "item": "Item",
        "volume": "Volume",
        "execution": "Execution",
        "cell_suspension": "Cell Suspension",
        "add_first": "Add first",
        "prepared_medium": "Prepared Medium",
        "add_after_to_reach": "Add after to reach {:.2f} ml total",
        "total_per_unit": "Total per Unit",
        "ready_for_flask": "Ready for one flask/plate",
        "language": "Language",
        "arabic": "العربية",
        "english": "English",
        "theme": "Theme",
        "light": "Light",
        "dark": "Dark",
        "num_units_singular": "flask",
        "num_units_plural": "flasks",
        "cell_unit": "cells",
        "flask_unit": "flask",
        "step": "Step",
        "serum": "Serum",
        "antibiotic": "Antibiotic",
        "other_supplements": "Other Supplements",
    },
    "ar": {
        "title": "🧫 آلة حاسبة لزراعة الخلايا",
        "intro": "أداة لحساب زراعة الخلايا (Primary culture & Passage)",
        "general_settings": "إعدادات عامة",
        "experiment_type": "اختر نوع التجربة:",
        "primary_culture": "Primary Culture",
        "passage": "Passage",
        "cell_line_selection": "اختيار خط الخلية",
        "select_cell_line": "اختر خط الخلية:",
        "custom": "مخصص",
        "new_cell_line_name": "اسم خط الخلية الجديد:",
        "cell_type": "نوع الخلية:",
        "adherent_cm2": "ملتصقة (لكل سم²)",
        "suspension_ml": "معلقة (لكل مل)",
        "seeding_density": "أدخل كثافة الزرع:",
        "add_new_cell_line": "➕ إضافة خط خلية جديد",
        "add_success": "تم إضافة {} بنجاح!",
        "add_error": "الرجاء إدخال اسم وكثافة صحيحة لخط الخلية.",
        "use_custom_seeding_density": "استخدام كثافة زرع مخصصة؟",
        "custom_seeding_density_input": "أدخل كثافة الزرع المخصصة (خلايا/سم² أو خلايا/مل):",
        "flask_settings": "إعدادات الفلاسك",
        "select_flask": "اختر الفلاسك:",
        "num_units": "عدد الوحدات (الفلاسكات/الأطباق):",
        "initial_cell_concentration": "تركيز المعلق الخلوي الابتدائي (خلايا/مل):",
        "split_ratio": "Split ratio (مثال: 1:3)",
        "split_ratio_error": "صيغة Split ratio غير صحيحة. استخدم 1:N",
        "total_medium_per_flask": "الحجم الكلي للوسط لكل {} (مل):",
        "medium_components": "مكونات الوسط",
        "base_medium_name": "اسم الوسط الأساسي:",
        "serum_percent": "Serum %:",
        "antibiotic_percent": "Antibiotic %:",
        "supplements_percent": "Other Supplements %:",
        "detailed_results": "📊 النتائج التفصيلية",
        "cell_calculation": "1️⃣ حساب الخلايا",
        "total_cells_needed": "عدد الخلايا الكلي المطلوب (للزرع)",
        "equation": "المعادلة",
        "result": "النتيجة",
        "practical_execution": "التنفيذ العملي",
        "cells_per_flask_after_split": "عدد الخلايا لكل فلاسك بعد Split Ratio (إذا كان {})",
        "volume_needed_for_cells": "حجم المعلق الخلوي المطلوب للوصول لـ {:,} خلية",
        "draw_ul_from_suspension": "اسحب {:,} µl من المعلق الخلوي",
        "total_medium_preparation": "2️⃣ تحضير الوسط الكلي",
        "component": "المكون",
        "percentage": "النسبة",
        "calculation": "الحساب",
        "final_volume": "الحجم النهائي",
        "add_ml": "أضف {:.2f} مل",
        "prepare_single_flask": "3️⃣ تحضير كل {} على حدة",
        "item": "العنصر",
        "volume": "الحجم",
        "execution": "التنفيذ",
        "cell_suspension": "المعلق الخلوي (Cell Suspension)",
        "add_first": "أضف أولًا",
        "prepared_medium": "الوسط المحضر (Prepared Medium)",
        "add_after_to_reach": "أضف بعده ليصبح المجموع {:.2f} مل",
        "total_per_unit": "الإجمالي لكل وحدة",
        "ready_for_flask": "جاهز للفلاسك/الطبق الواحد",
        "language": "اللغة",
        "arabic": "العربية",
        "english": "الإنجليزية",
        "theme": "السمة",
        "light": "فاتح",
        "dark": "داكن",
        "num_units_singular": "فلاسك",
        "num_units_plural": "فلاسكات",
        "cell_unit": "خلية",
        "flask_unit": "فلاسك",
        "step": "الخطوة",
        "serum": "Serum",
        "antibiotic": "Antibiotic",
        "other_supplements": "Other Supplements",
    }
}

# --- Helper function ---
def format_ml_ul(value_ml):
    """تحويل ml إلى نص يحتوي ml و µl"""
    value_ul = value_ml * 1000
    return f"{value_ml:.2f} ml ({int(value_ul)} µl)"

def format_scientific_notation(number):
    """Formats a number from scientific notation (e.g., 3.0e+04) to '3 x 10^4'"""
    if number == 0:
        return "0"
    
    # Get the exponent
    exponent = 0
    if number != 0:
        exponent = int(f"{number:e}".split('e')[-1])

    # Get the base number
    base = number / (10**exponent)
    
    # Format the base to avoid trailing .0 if it's an integer
    if base == int(base):
        base_str = str(int(base))
    else:
        base_str = f"{base:.1f}" # Keep one decimal place if not integer

    if exponent == 0:
        return base_str
    elif exponent == 1:
        return f"{base_str} × 10"
    else:
        return f"{base_str} × 10^{exponent}"

# --- Reference Data ---
# Combined cell lines from both ts.py and انسجة.html
if 'cell_lines' not in st.session_state:
    st.session_state.cell_lines = {
        "HeLa": {"type": "adherent", "density": 3e4},     # per cm² (from ts.py)
        "HEK293": {"type": "adherent", "density": 2.5e4}, # from ts.py
        "MCF-7": {"type": "adherent", "density": 3e4},    # from ts.py
        "A549": {"type": "adherent", "density": 2.5e4},    # from ts.py
        "Jurkat": {"type": "suspension", "density": 3e5}, # per ml (from ts.py)
        # Additional from انسجة.html (using a placeholder type for now, will be updated by custom input)
        "CHO": {"type": "adherent", "density": 20000},
        "Vero": {"type": "adherent", "density": 12000},
        "NIH-3T3": {"type": "adherent", "density": 4000},
        "HUVEC": {"type": "adherent", "density": 10000},
        "iPSC": {"type": "adherent", "density": 30000},
    }

flask_data = {
    "T25": {"area": 25, "media": 5},
    "T75": {"area": 75, "media": 15},
    "T175": {"area": 175, "media": 30}, # Assuming a default media volume
    "6well": {"area": 9.5, "media": 2},
    "96well": {"area": 0.32, "media": 0.2},
}

# --- UI ---
# Language selection
if 'lang' not in st.session_state:
    st.session_state.lang = "ar"

lang_options = {"ar": "العربية", "en": "English"}
selected_lang_key = st.sidebar.radio(MESSAGES[st.session_state.lang]["language"], list(lang_options.keys()), format_func=lambda x: lang_options[x], key="lang_selector")
st.session_state.lang = selected_lang_key
_ = MESSAGES[st.session_state.lang]

# Theme selection
if 'theme' not in st.session_state:
    st.session_state.theme = "dark" # Default theme

theme_options = {"light": _["light"], "dark": _["dark"]}
selected_theme_key = st.sidebar.radio(_["theme"], list(theme_options.keys()), format_func=lambda x: theme_options[x], key="theme_selector")
st.session_state.theme = selected_theme_key

if st.session_state.lang == "ar":
    st.markdown(
        """
        <style>
        html, body, [data-testid="stAppViewContainer"], [data-testid="stSidebar"] {
            direction: rtl;
            text-align: right;
        }
        [data-testid="stSidebar"] .stRadio > label {
            text-align: right;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

st.title(_["title"])
st.markdown(_["intro"])

with st.sidebar:
    st.header(_["general_settings"])
    mode = st.radio(_["experiment_type"], [_[f"primary_culture"], _["passage"]])

    st.subheader(_["cell_line_selection"])
    cell_line_options = list(st.session_state.cell_lines.keys()) + [(_["custom"])]
    selected_cell_line_name = st.selectbox(_["select_cell_line"], cell_line_options)

    # Custom cell line input
    if selected_cell_line_name == _["custom"]:
        custom_cell_name = st.text_input(_["new_cell_line_name"])
        custom_cell_type = st.radio(_["cell_type"], [_[f"adherent_cm2"], _["suspension_ml"]])
        custom_density_input = st.number_input(_["seeding_density"], value=20000.0, step=1000.0, format="%.0f", key="custom_density_input")
        if st.button(_["add_new_cell_line"]):
            if custom_cell_name and custom_density_input > 0:
                cell_line_type_val = "adherent" if _["adherent_cm2"] in custom_cell_type else "suspension"
                st.session_state.cell_lines[custom_cell_name] = {"type": cell_line_type_val, "density": custom_density_input}
                st.success(_["add_success"].format(custom_cell_name))
                selected_cell_line_name = custom_cell_name # Select the newly added line
                st.experimental_rerun() # Rerun to update selectbox
            else:
                st.error(_["add_error"])
    
    # Determine current cell line properties
    if selected_cell_line_name != _["custom"] and selected_cell_line_name in st.session_state.cell_lines:
        cell_line_type = st.session_state.cell_lines[selected_cell_line_name]["type"]
        default_density = st.session_state.cell_lines[selected_cell_line_name]["density"]
    else: # Fallback for custom or if not yet added
        cell_line_type = "adherent" if _["adherent_cm2"] in custom_cell_type else "suspension"
        default_density = custom_density_input # Use the input value for custom cell line

    use_custom_seeding_density = st.checkbox(_["use_custom_seeding_density"])
    if use_custom_seeding_density:
        density = st.number_input(
            _["custom_seeding_density_input"],
            value=float(default_density),
            step=1000.0,
            format="%.0f",
            key="user_custom_density"
        )
    else:
        density = default_density

    st.subheader(_["flask_settings"])
    flask_type = st.selectbox(_["select_flask"], list(flask_data.keys()))
    flask_area = flask_data[flask_type]["area"]
    
    num_flasks = st.number_input(_["num_units"], value=1, min_value=1, step=1)

    initial_cell_concentration = st.number_input(_["initial_cell_concentration"], value=2_000_000, step=100000, format="%.0f")

    split_ratio_val = 1
    if mode == _["passage"]:
        split_ratio_input = st.text_input(_["split_ratio"], value="1:3")
        if split_ratio_input:
            try:
                parts = split_ratio_input.split(':')
                if len(parts) == 2 and int(parts[1]) > 0:
                    split_ratio_val = int(parts[1])
                else:
                    st.warning(_["split_ratio_error"])
            except ValueError:
                st.warning(_["split_ratio_error"])

    medium_total_ml_per_flask = st.number_input(
        _["total_medium_per_flask"].format(flask_type),
        value=float(flask_data[flask_type]["media"]),
        step=0.5
    )
    medium_total_ml = medium_total_ml_per_flask * num_flasks

    st.subheader(_["medium_components"])
    base_media_name = st.text_input(_["base_medium_name"], value="DMEM")
    serum_percent = st.number_input(_["serum_percent"], value=9, step=1, max_value=100)
    antibiotic_percent = st.number_input(_["antibiotic_percent"], value=1, step=1, max_value=100)
    supplements_percent = st.number_input(_["supplements_percent"], value=0, step=1, max_value=100)

# --- Calculations ---
total_seeding_cells_needed = 0
if cell_line_type == "adherent":
    total_seeding_cells_needed = density * flask_area * num_flasks
else: # suspension
    total_seeding_cells_needed = density * medium_total_ml # For suspension, density is per ml, so multiply by total media volume

cells_per_flask_after_split = total_seeding_cells_needed
if mode == _["passage"]:
    cells_per_flask_after_split = total_seeding_cells_needed / split_ratio_val

volume_needed_from_stock_ml = 0
if initial_cell_concentration > 0:
    volume_needed_from_stock_ml = cells_per_flask_after_split / initial_cell_concentration
volume_needed_from_stock_ul = volume_needed_from_stock_ml * 1000

# Medium components
serum_ml = medium_total_ml * serum_percent / 100
antibiotic_ml = medium_total_ml * antibiotic_percent / 100
supplements_ml = medium_total_ml * supplements_percent / 100
base_media_ml = medium_total_ml - (serum_ml + antibiotic_ml + supplements_ml)

# Final medium for one flask (considering cell suspension volume)
final_medium_ml_for_one_flask = medium_total_ml_per_flask - (volume_needed_from_stock_ml / num_flasks)


# --- Results ---
st.header(_["detailed_results"])

st.subheader(_["cell_calculation"])
df1 = pd.DataFrame([
    [_["total_cells_needed"],
     f"({format_scientific_notation(density)}) × {flask_area} cm² × {num_flasks} {_['num_units_singular'] if num_flasks == 1 else _['num_units_plural']}",
     f"{int(total_seeding_cells_needed):,} {_['cell_unit']}",
     "—"],
    [f"{_['cells_per_flask_after_split'].format(mode)}",
     f"{int(total_seeding_cells_needed):,} ÷ {split_ratio_val}",
     f"{int(cells_per_flask_after_split):,} {_['cell_unit']}/{_['flask_unit']}",
     "—"],
    [f"{_['volume_needed_for_cells'].format(int(cells_per_flask_after_split))}",
     f"{int(cells_per_flask_after_split):,} ÷ {initial_cell_concentration:,}",
     f"{volume_needed_from_stock_ml:.2f} ml",
     f"{_['draw_ul_from_suspension'].format(int(volume_needed_from_stock_ul))}"],
], columns=[_["step"], _["equation"], _["result"], _["practical_execution"]])
st.table(df1)

st.subheader(_["total_medium_preparation"])
df2 = pd.DataFrame([
    [_["base_medium_name"], "—", f"{medium_total_ml:.2f} – ({serum_ml:.2f} + {antibiotic_ml:.2f} + {supplements_ml:.2f})", f"{base_media_ml:.2f} ml", f"{int(base_media_ml * 1000)} µl"],
    [_["serum"], f"{serum_percent}%", f"{medium_total_ml:.2f} × {serum_percent/100:.2f}", f"{serum_ml:.2f} ml", f"{int(serum_ml * 1000)} µl"],
    [_["antibiotic"], f"{antibiotic_percent}%", f"{medium_total_ml:.2f} × {antibiotic_percent/100:.2f}", f"{antibiotic_ml:.2f} ml", f"{int(antibiotic_ml * 1000)} µl"],
    [_["other_supplements"], f"{supplements_percent}%", "—", f"{supplements_ml:.2f} ml", f"{int(supplements_ml * 1000)} µl"],
], columns=[_["component"], _["percentage"], _["calculation"], _["final_volume"], _["practical_execution"]])
st.table(df2)

st.subheader(f"{_['prepare_single_flask'].format(flask_type)}")
df3 = pd.DataFrame([
    [_["cell_suspension"], f"{(volume_needed_from_stock_ml / num_flasks):.2f} ml ({int((volume_needed_from_stock_ml / num_flasks) * 1000)} µl)", _["add_first"]],
    [_["prepared_medium"], f"{final_medium_ml_for_one_flask:.2f} ml ({int(final_medium_ml_for_one_flask * 1000)} µl)", _["add_after_to_reach"].format(medium_total_ml_per_flask)],
    [_["total_per_unit"], f"{medium_total_ml_per_flask:.2f} ml ({int(medium_total_ml_per_flask * 1000)} µl)", _["ready_for_flask"]],
], columns=[_["item"], _["volume"], _["execution"]])
st.table(df3)