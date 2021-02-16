import xlsxwriter
import xlrd
import time

start = time.time()

for u in range(33):
    path = "food_10.xls"

    inputWorkbook = xlrd.open_workbook(path)
    inputWorksheet = inputWorkbook.sheet_by_index(0)

    outWorkbook = xlsxwriter.Workbook("Test1.xlsx")
    outSheet = outWorkbook.add_worksheet()

    spalten = inputWorksheet.ncols
    zeilen = inputWorksheet.nrows

    print(spalten)
    print(zeilen)


    product_name = []
    quantity = []
    brands = []
    categories = []
    categories_en = []
    countries = []
    countries_en = []
    nutriscore_score = []
    nutriscore_grade = []
    energy_kj_100g = []
    energy_kcal_100g = []
    energy_100g = []
    energy_from_fat_100g = []
    fat_100g = []
    saturated_fat_100g = []
    butyric_acid_100g = []
    caproic_acid_100g = []
    caprylic_acid_100g = []
    capric_acid_100g = []
    lauric_acid_100g = []
    myristic_acid_100g = []
    palmitic_acid_100g = []
    stearic_acid_100g = []
    arachidic_acid_100g = []
    behenic_acid_100g = []
    lignoceric_acid_100g = []
    cerotic_acid_100g = []
    montanic_acid_100g = []
    melissic_acid_100g = []
    monounsaturated_fat_100g = []
    polyunsaturated_fat_100g = []
    omega_3_fat_100g = []
    alpha_linolenic_acid_100g = []
    eicosapentaenoic_acid_100g = []
    docosahexaenoic_acid_100g = []
    omega_6_fat_100g = []
    linoleic_acid_100g = []
    arachidonic_acid_100g = []
    gamma_linolenic_acid_100g = []
    dihomo_gamma_linolenic_acid_100g = []
    omega_9_fat_100g = []
    oleic_acid_100g = []
    elaidic_acid_100g = []
    gondoic_acid_100g = []
    mead_acid_100g = []
    erucic_acid_100g = []
    nervonic_acid_100g = []
    trans_fat_100g = []
    cholesterol_100g = []
    carbohydrates_100g = []
    sugars_100g = []
    sucrose_100g = []
    glucose_100g = []
    fructose_100g = []
    lactose_100g = []
    maltose_100g = []
    maltodextrins_100g = []
    starch_100g = []
    polyols_100g = []
    fiber_100g = []
    soluble_fiber_100g = []
    insoluble_fiber_100g = []
    proteins_100g = []
    casein_100g = []
    serum_proteins_100g = []
    nucleotides_100g = []
    salt_100g = []
    sodium_100g = []
    alcohol_100g = []
    vitamin_a_100g = []
    beta_carotene_100g = []
    vitamin_d_100g = []
    vitamin_e_100g = []
    vitamin_k_100g = []
    vitamin_c_100g = []
    vitamin_b1_100g = []
    vitamin_b2_100g = []
    vitamin_pp_100g = []
    vitamin_b6_100g = []
    vitamin_b9_100g = []
    folates_100g = []
    vitamin_b12_100g = []
    biotin_100g = []
    pantothenic_acid_100g = []
    silica_100g = []
    bicarbonate_100g = []
    potassium_100g = []
    chloride_100g = []
    calcium_100g = []
    phosphorus_100g = []
    iron_100g = []
    magnesium_100g = []
    zinc_100g = []
    copper_100g = []
    manganese_100g = []
    fluoride_100g = []
    selenium_100g = []
    chromium_100g = []
    molybdenum_100g = []
    iodine_100g = []
    caffeine_100g = []
    taurine_100g = []
    ph_100g = []
    fruits_vegetables_nuts_100g = []
    fruits_vegetables_nuts_dried_100g = []
    fruits_vegetables_nuts_estimate_100g = []
    collagen_meat_protein_ratio_100g = []
    cocoa_100g = []
    chlorophyl_100g = []
    carbon_footprint_100g = []
    carbon_footprint_from_meat_or_fish_100g = []
    nutrition_score_fr_100g = []
    nutrition_score_uk_100g = []
    glycemic_index_100g = []
    water_hardness_100g = []
    choline_100g = []
    phylloquinone_100g = []
    beta_glucan_100g = []
    inositol_100g = []
    carnitine_100g = []

    test = []
    test1 = [] 
    h = 0
    counter = 0
    for x in range(zeilen):
        name = inputWorksheet.cell_value(h, 7)
        mänge = inputWorksheet.cell_value(h, 10)
        kcal = inputWorksheet.cell_value(h, 74)
        kohlhy = inputWorksheet.cell_value(h, 113)
        fett = inputWorksheet.cell_value(h, 77)
        protein = inputWorksheet.cell_value(h, 126)
        if len(name) > 0:
            if len(mänge) > 0:
                if type(kcal) == int or type(kcal) == float:
                    if type(kohlhy) == int or type(kohlhy) == float:
                        if type(fett) == int or type(fett) == float:
                            if type(protein) == int or type(protein) == float:
                                product_name.append(name)
                                quantity.append(mänge)
                                energy_kcal_100g.append(kcal)
                                carbohydrates_100g.append(kohlhy)
                                fat_100g.append(fett)
                                proteins_100g.append(protein)
                            else:
                                #print("Keine Proteine")
                                counter += 1
                        else:
                        # print("Kein Fett")
                            counter += 1
                    else:
                        #print("Keine Kohlenhydrate")
                        counter += 1
                else:
                    #print("Keine Kcal")
                    counter += 1
            else:
                #print("Keine Mänge" + " / " + mänge)
                counter += 1
        else:
            #print("Kein Name")
            counter += 1
        h += 1

    #print(test)
    print(len(test))
    print(zeilen)

    outSheet.write(0, 0, "Product Name")
    outSheet.write(0, 1, "Quantity")
    outSheet.write(0, 2, "Kcal")
    outSheet.write(0, 3, "Carbonhydrates")
    outSheet.write(0, 4, "Fat")
    outSheet.write(0, 5, "Protein")

    h = 1
    j = 0
    for i in range(len(product_name)):
        outSheet.write(h, 0, product_name[j])
        outSheet.write(h, 1, quantity[j])
        outSheet.write(h, 2, energy_kcal_100g[j])
        outSheet.write(h, 3, carbohydrates_100g[j])
        outSheet.write(h, 4, fat_100g[j])
        outSheet.write(h, 5, proteins_100g[j])
        h += 1
        j += 1
    outWorkbook.close()
    print(counter)
end = time.time()
print(end - start)