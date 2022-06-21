import headlinesfunction as hd
import pandas as pd
import numpy as np
import circlify
import matplotlib.pyplot as plt


# Most reported political party

if False:
    bjp = ["bjp","Bharatiya Janata Party"]
    inc = ["INC","Congress"]
    aap = ["AAP","Aam Aadmi Party"]
    cpi = ["CPI","Communist Party of India"]
    bsp = ["BSP","Bahujan Samaj Party"]
    dmk = ["DMK","Dravida Munnetra Kazhagam"]
    shivsena = ["sena","shiv sena"]

    data = {'Party': ['BJP', 'INC', 'AAP', 'CPI', 'BSP', 'DMK', 'SHIV SENA'],
            'Reported': [hd.countOccurancesAny(bjp),hd.countOccurancesAny(inc),hd.countOccurancesAny(aap),hd.countOccurancesAny(cpi),hd.countOccurancesAny(bsp),hd.countOccurancesAny(dmk),hd.countOccurancesAny(shivsena)]}
    df = pd.DataFrame(data)
    print(df.sort_values("Reported",ascending=False))

#   RESULTS:                
#          Party  Reported
#   1        INC     10413
#   0        BJP     10285
#   6  SHIV SENA      2457
#   5        DMK      1107
#   4        BSP       794
#   3        CPI       569
#   2        AAP       137

# Most Reported Politician 
if False:
    modi = ["Modi","Narendra Modi","Narendra Damodardas Modi"]
    amitshah = ["amit shah","shah"]
    rajnath = ["rajnath singh"]
    jaishankar = ["jaishankar"]
    mamata = ["mamata","didi"]
    kejriwal = ["aravind","kejriwal"]
    yogi = ["adityanath","yogi","ajay bisht"]
    rahul = ["rahul"]
    stalin = ["stalin"]
    akhilesh = ["akhilesh"]
    owaisi = ["owaisi"]
    gehlot = ["gehlot"]
    biswa = ["himanta biswa","biswa"]
    scindia = ["scindia"]
    sibal = ["sibal"]
    manmohan = ["manmohan singh"]
    mayavati = ["mayavati"]
    mulayam = ["mulayam"]
    naveen = ["patnaik"]
    nitish = ["nitish"]
    sonia = ["sonia"]
    uddhav = ["uddhav"]

    data = {
        'Political' : ['Narendra Modi','Amit Shah','Rajnath Singh','S Jaishankar',
        'Mamata Bannerjee','Aravind Kejrival','Yogi Adityanath','Rahul Gandhi','MK Stalin',
        'Akhilesh Yadav','Asaduddin Owaisi','Ashok Gehlot','Himanta Biswa Sarma', 'Jotiraditya Scindia',
        'Kapil Sibal','Manmohan Singh','Mayavati','Mulayam Singh Yadav','Naveen Patnaik','Nitish Kumar','Sonia Gandhi','Uddhav Thackeray'],
        'Reported' : [hd.countOccurancesAny(modi),hd.countOccurancesAny(amitshah),hd.countOccurancesAny(rajnath),hd.countOccurancesAny(jaishankar),
        hd.countOccurancesAny(mamata),
        hd.countOccurancesAny(kejriwal),hd.countOccurancesAny(yogi),hd.countOccurancesAny(rahul),hd.countOccurancesAny(stalin),
        hd.countOccurancesAny(akhilesh),hd.countOccurancesAny(owaisi),hd.countOccurancesAny(gehlot),hd.countOccurancesAny(biswa),hd.countOccurancesAny(scindia),
        hd.countOccurancesAny(sibal),hd.countOccurancesAny(manmohan),hd.countOccurancesAny(mayavati),hd.countOccurancesAny(mulayam),hd.countOccurancesAny(naveen),
        hd.countOccurancesAny(nitish),hd.countOccurancesAny(sonia),hd.countOccurancesAny(uddhav)]
    }
    df = pd.DataFrame(data)
    print(df.sort_values("Reported",ascending=False))
    # df.to_csv(r'X:/tempforgraph.csv')

#                  Political  Reported
#    0         Narendra Modi      3619
#    20         Sonia Gandhi      3113
#    4      Mamata Bannerjee      1737
#    5      Aravind Kejrival      1729
#    7          Rahul Gandhi      1723
#    1             Amit Shah      1049
#    19         Nitish Kumar       986
#    17  Mulayam Singh Yadav       944
#    14          Kapil Sibal       452
#    9        Akhilesh Yadav       244
#    15       Manmohan Singh       196
#    11         Ashok Gehlot       151
#    21     Uddhav Thackeray       149
#    18       Naveen Patnaik       116
#    8             MK Stalin       103
#    6       Yogi Adityanath       102
#    13  Jotiraditya Scindia        94
#    2         Rajnath Singh        73
#    12  Himanta Biswa Sarma        72
#    10     Asaduddin Owaisi        14
#    16             Mayavati         1
#    3          S Jaishankar         1


# Making Circle Packing Graph
if False:
    # compute circle positions:
    circles = circlify.circlify(
        df['Reported'].tolist(), 
        show_enclosure=False, 
        target_enclosure=circlify.Circle(x=0, y=0, r=1)
    )

    # Create just a figure and only one subplot
    fig, ax = plt.subplots(figsize=(10,10))

    # Remove axes
    ax.axis('off')

    # Find axis boundaries
    lim = max(
        max(
            abs(circle.x) + circle.r,
            abs(circle.y) + circle.r,
        )
        for circle in circles
    )
    plt.xlim(-lim, lim)
    plt.ylim(-lim, lim)

    # list of labels
    labels = df['Reported']

    # print circles
    for circle, label in zip(circles, labels):
        x, y, r = circle
        ax.add_patch(plt.Circle((x, y), r, alpha=0.2, linewidth=2))
        plt.annotate(
            label, 
            (x,y ) ,
            va='center',
            ha='center'
        )

    plt.show()


# Crime Statistics

if False:
    robbery = ['robbery','thief','thieves','chori']
    sexual = ['rape','rapist','sexual assault']
    dowry = ['dowry','dahej']
    drugs = ['drug']
    traffick = ['traffick']
    cyber = ['hack','cyber crime','phish']
    murder = ['murder']

    data = {
        'Crime':['Robbery','Sexual','Dowry',"Drugs",'Trafficking','Cyber','Murder'],
        'Reported':[hd.countOccurancesAny(robbery),hd.countOccurancesAny(sexual),hd.countOccurancesAny(dowry),hd.countOccurancesAny(drugs)
        ,hd.countOccurancesAny(traffick),hd.countOccurancesAny(cyber),hd.countOccurancesAny(murder)]
    }
    df = pd.DataFrame(data)
    print(df.sort_values("Reported",ascending=False))

#            Crime  Reported
#   6       Murder      3271
#   1       Sexual      2533
#   5        Cyber      1538
#   3        Drugs      1403
#   0      Robbery       384
#   2        Dowry       217
#   4  Trafficking       170

# States Stats

if False:
    UttarPradesh = ['Uttar Pradesh', ' UP ',"Agra" ,"Aligarh" ,"Ambedkar Nagar" ,"Amethi" ,"Amroha" ,"Auraiya" ,"Ayodhya" ,"Azamgarh" ,"Baghpat" ,"Bahraich" ,"Ballia" ,"Balrampur" ,"Barabanki" ,"Bareilly" ,"Bhadohi" ,"Bijnor" ,"Budaun" ,"Bulandshahr" ,"Chandauli" ,"Chitrakoot" ,"Deoria" ,"Etah" ,"Etawah" ,"Farrukhabad" ,"Fatehpur" ,"Firozabad" ,"Gautam Buddha Nagar" ,"Ghaziabad" ,"Ghazipur" ,"Gorakhpur" ,"Hamirpur" ,"Hardoi" ,"Hathras" ,"Jalaun" ,"Jaunpur" ,"Jhansi" ,"Kannauj" ,"Kanpur Dehat" ,"Kanpur Nagar" ,"Kasganj" ,"Kaushambi" ,"Kushinagar" ,"Lalitpur" ,"Lucknow" ,"Maharajganj" ,"Mahoba" ,"Mainpuri" ,"Mathura" ,"Meerut" ,"Mirzapur" ,"Moradabad" ,"Muzaffarnagar" ,"Pilibhit" ,"Pratapgarh" ,"Prayagraj" ,"Raebareli" ,"Rampur" ,"Saharanpur" ,"Sambhal" ,"Sant Kabir Nagar" ,"Shahjahanpur" ,"Shamli" ,"Shravasti" ,"Siddharthnagar" ,"Sitapur" ,"Sonbhadra" ,"Sultanpur" ,"Unnao" ,"Varanasi" ]
    AndamanNicobar = ["Andaman","Nicobar"]
    AndhraPradesh = ["Andhra","Anantapur" ,"Chittoor" ,"East Godavari" ,"Alluri Sitarama Raju" ,"Anakapalli" ,"Annamaya" ,"Bapatla" ,"Eluru" ,"Guntur" ,"Kadapa" ,"Kakinada" ,"Konaseema" ,"Krishna" ,"Kurnool" ,"Manyam" ,"N T Rama Rao" ,"Nandyal" ,"Nellore" ,"Palnadu" ,"Prakasam" ,"Sri Balaji" ,"Sri Satya Sai" ,"Srikakulam" ,"Visakhapatnam" ,"Vizianagaram" ,"West Godavari"]
    ArunachalPradesh = ['Arunachal',"Anjaw" ,"Changlang" ,"Dibang Valley" ,"East Kameng" ,"East Siang" ,"Kamle" ,"Kra Daadi" ,"Kurung Kumey" ,"Lepa Rada" ,"Lohit" ,"Longding" ,"Lower Dibang Valley" ,"Lower Siang" ,"Lower Subansiri" ,"Namsai" ,"Pakke Kessang" ,"Papum Pare" ,"Shi Yomi" ,"Siang" ,"Tawang" ,"Tirap" ,"Upper Siang" ,"Upper Subansiri" ,"West Kameng" ,"West Siang" ]
    Assam = ['assam',"Bajali" ,"Baksa" ,"Barpeta" ,"Biswanath" ,"Bongaigaon" ,"Cachar" ,"Charaideo" ,"Chirang" ,"Darrang" ,"Dhemaji" ,"Dhubri" ,"Dibrugarh" ,"Dima Hasao" ,"Goalpara" ,"Golaghat" ,"Hailakandi" ,"Hojai" ,"Jorhat" ,"Kamrup" ,"Kamrup Metropolitan" ,"Karbi Anglong" ,"Karimganj" ,"Kokrajhar" ,"Lakhimpur" ,"Majuli" ,"Morigaon" ,"Nagaon" ,"Nalbari" ,"Sivasagar" ,"Sonitpur" ,"South Salmara-Mankachar" ,"Tinsukia" ,"Udalguri" ,"West Karbi Anglong" ]    
    Bihar = ['bihar', "Araria" ,"Arwal" ,"Aurangabad" ,"Banka" ,"Begusarai" ,"Bhagalpur" ,"Bhojpur" ,"Buxar" ,"Darbhanga" ,"East Champaran" ,"Gaya" ,"Gopalganj" ,"Jamui" ,"Jehanabad" ,"Kaimur" ,"Katihar" ,"Khagaria" ,"Kishanganj" ,"Lakhisarai" ,"Madhepura" ,"Madhubani" ,"Munger" ,"Muzaffarpur" ,"Nalanda" ,"Nawada" ,"Patna" ,"Purnia" ,"Rohtas" ,"Saharsa" ,"Samastipur" ,"Saran" ,"Sheikhpura" ,"Sheohar" ,"Sitamarhi" ,"Siwan" ,"Supaul" ,"Vaishali" ,"West Champaran"]
    Chandigarh = ['Chandigarh']
    Chhattisgarh = ['Chhattisgarh', "Balod" ,"Baloda Bazar" ,"Balrampur" ,"Bastar" ,"Bemetara" ,"Bijapur" ,"Bilaspur" ,"Dantewada" ,"Dhamtari" ,"Durg" ,"Gariaband" ,"Gaurela Pendra Marwahi" ,"Janjgir Champa" ,"Jashpur" ,"Kabirdham" ,"Kanker" ,"Kondagaon" ,"Korba" ,"Koriya" ,"Mahasamund" ,"Manendragarh" ,"Mohla Manpur" ,"Mungeli" ,"Narayanpur" ,"Raigarh" ,"Raipur" ,"Rajnandgaon" ,"Sakti" ,"Sarangarh Bilaigarh" ,"Sukma" ,"Surajpur"]
    Dadra = ['Dadra', 'Daman', 'Diu']
    Delhi = ['Delhi']
    Goa = ['Goa']
    Gujrat = ['Gujrat', "Ahmedabad" ,"Amreli" ,"Anand" ,"Aravalli" ,"Banaskantha" ,"Bharuch" ,"Bhavnagar" ,"Botad" ,"Chhota Udaipur" ,"Dahod" ,"Dang" ,"Devbhoomi Dwarka" ,"Gandhinagar" ,"Gir Somnath" ,"Jamnagar" ,"Junagadh" ,"Kheda" ,"Kutch" ,"Mahisagar" ,"Mehsana" ,"Morbi" ,"Narmada" ,"Navsari" ,"Panchmahal" ,"Patan" ,"Porbandar" ,"Rajkot" ,"Sabarkantha" ,"Surat" ,"Surendranagar" ,"Tapi" ,"Vadodara" ,"Valsad"]
    Haryana = ['Haryana', "Ambala" ,"Bhiwani" ,"Charkhi Dadri" ,"Faridabad" ,"Fatehabad" ,"Gurugram" ,"Hisar" ,"Jhajjar" ,"Jind" ,"Kaithal" ,"Karnal" ,"Kurukshetra" ,"Mahendragarh" ,"Mewat" ,"Palwal" ,"Panchkula" ,"Panipat" ,"Rewari" ,"Rohtak" ,"Sirsa" ,"Sonipat" ,"Yamunanagar"]
    HimachalPradesh = ['Himachal',"Bilaspur" ,"Chamba" ,"Hamirpur" ,"Kangra" ,"Kinnaur" ,"Kullu" ,"Lahaul Spiti" ,"Mandi" ,"Shimla" ,"Sirmaur" ,"Solan" ,"Una" ]
    JammuKashmir = ["Jammu", "Kashmir", "J&K", "JK", "Anantnag" ,"Bandipora" ,"Baramulla" ,"Budgam" ,"Doda" ,"Ganderbal" ,"Jammu" ,"Kathua" ,"Kishtwar" ,"Kulgam" ,"Kupwara" ,"Poonch" ,"Pulwama" ,"Rajouri" ,"Ramban" ,"Reasi" ,"Samba" ,"Shopian" ,"Srinagar" ,"Udhampur"]
    Jharkand = ["Jharkand", "Bokaro" ,"Chatra" ,"Deoghar" ,"Dhanbad" ,"Dumka" ,"East Singhbhum" ,"Garhwa" ,"Giridih" ,"Godda" ,"Gumla" ,"Hazaribagh" ,"Jamtara" ,"Khunti" ,"Koderma" ,"Latehar" ,"Lohardaga" ,"Pakur" ,"Palamu" ,"Ramgarh" ,"Ranchi" ,"Sahebganj" ,"Seraikela Kharsawan" ,"Simdega" ,"West Singhbhum"]
    Karnataka = ['Karnataka',"Bagalkot" ,"Bangalore Rural" ,"Bangalore Urban" ,"Belgaum" ,"Bellary" ,"Bidar" ,"Chamarajanagar" ,"Chikkaballapur" ,"Chikkamagaluru" ,"Chitradurga" ,"Dakshina Kannada" ,"Davanagere" ,"Dharwad" ,"Gadag" ,"Gulbarga" ,"Hassan" ,"Haveri" ,"Kodagu" ,"Kolar" ,"Koppal" ,"Mandya" ,"Mysore" ,"Raichur" ,"Ramanagara" ,"Shimoga" ,"Tumkur" ,"Udupi" ,"Uttara Kannada" ,"Vijayanagara" ,"Vijayapura" ,"Yadgir"]
    Kerala = ['Kerala', "Alappuzha" ,"Ernakulam" ,"Idukki" ,"Kannur" ,"Kasaragod" ,"Kollam" ,"Kottayam" ,"Kozhikode" ,"Malappuram" ,"Palakkad" ,"Pathanamthitta" ,"Thiruvananthapuram" ,"Thrissur" ,"Wayanad"]
    Ladakh = ['Ladakh','leh','kargil']
    Lakshadweep = ['Lakshadweep']
    MadhyaPradesh = ["Madhya", "Agar Malwa" ,"Alirajpur" ,"Anuppur" ,"Ashoknagar" ,"Balaghat" ,"Barwani" ,"Betul" ,"Bhind" ,"Bhopal" ,"Burhanpur" ,"Chachaura" ,"Chhatarpur" ,"Chhindwara" ,"Damoh" ,"Datia" ,"Dewas" ,"Dhar" ,"Dindori" ,"Guna" ,"Gwalior" ,"Harda" ,"Hoshangabad" ,"Indore" ,"Jabalpur" ,"Jhabua" ,"Katni" ,"Khandwa" ,"Khargone" ,"Maihar" ,"Mandla" ,"Mandsaur" ,"Morena" ,"Nagda" ,"Narsinghpur" ,"Neemuch" ,"Niwari" ,"Panna" ,"Raisen" ,"Rajgarh" ,"Ratlam" ,"Rewa" ,"Sagar" ,"Satna" ,"Sehore" ,"Seoni" ,"Shahdol" ,"Shajapur" ,"Sheopur" ,"Shivpuri" ,"Sidhi" ,"Singrauli" ,"Tikamgarh" ,"Ujjain" ,"Umaria" ,"Vidisha"]
    Maharashtra = ["Maharashtra", "Bombay", "Ahmednagar" ,"Akola" ,"Amravati" ,"Aurangabad" ,"Beed" ,"Bhandara" ,"Buldhana" ,"Chandrapur" ,"Dhule" ,"Gadchiroli" ,"Gondia" ,"Hingoli" ,"Jalgaon" ,"Jalna" ,"Kolhapur" ,"Latur" ,"Mumbai" ,"Mumbai Suburban" ,"Nagpur" ,"Nanded" ,"Nandurbar" ,"Nashik" ,"Osmanabad" ,"Palghar" ,"Parbhani" ,"Pune" ,"Raigad" ,"Ratnagiri" ,"Sangli" ,"Satara" ,"Sindhudurg" ,"Solapur" ,"Thane" ,"Wardha" ,"Washim" ,"Yavatmal"]
    Manipur = ['Manipur', "Bishnupur" ,"Chandel" ,"Churachandpur" ,"Imphal East" ,"Imphal West" ,"Jiribam" ,"Kakching" ,"Kamjong" ,"Kangpokpi" ,"Noney" ,"Pherzawl" ,"Senapati" ,"Tamenglong" ,"Tengnoupal" ,"Thoubal" ,"Ukhrul"]
    Meghalaya = ['Megh', "East Garo Hills" ,"East Jaintia Hills" ,"East Khasi Hills" ,"Mairang" ,"North Garo Hills" ,"Ri Bhoi" ,"South Garo Hills" ,"South West Garo Hills" ,"South West Khasi Hills" ,"West Garo Hills" ,"West Jaintia Hills" ,"West Khasi Hills"]
    Mizoram = ['Mizoram', "Aizawl" ,"Champhai" ,"Hnahthial" ,"Khawzawl" ,"Kolasib" ,"Lawngtlai" ,"Lunglei" ,"Mamit" ,"Saiha" ,"Saitual" ,"Serchhip" ]
    Nagaland = ['Nagaland', "Chumukedima" ,"Dimapur" ,"Kiphire" ,"Kohima" ,"Longleng" ,"Mokokchung" ,"Niuland" ,"Noklak" ,"Peren" ,"Phek" ,"Tseminyu" ,"Tuensang" ,"Wokha" ,"Zunheboto"]
    Odisha = ['Odisha', "Angul" ,"Balangir" ,"Balasore" ,"Bargarh" ,"Bhadrak" ,"Boudh" ,"Cuttack" ,"Debagarh" ,"Dhenkanal" ,"Gajapati" ,"Ganjam" ,"Jagatsinghpur" ,"Jajpur" ,"Jharsuguda" ,"Kalahandi" ,"Kandhamal" ,"Kendrapara" ,"Kendujhar" ,"Khordha" ,"Koraput" ,"Malkangiri" ,"Mayurbhanj" ,"Nabarangpur" ,"Nayagarh" ,"Nuapada" ,"Puri" ,"Rayagada" ,"Sambalpur" ,"Subarnapur" ,"Sundergarh"]
    Puducherry = ['Puducherry', "Karaikal" ,"Mahe" ,"Puducherry" ,"Yanam" ]
    Punjab = ['Punjab', "Amritsar" ,"Barnala" ,"Bathinda" ,"Faridkot" ,"Fatehgarh Sahib" ,"Fazilka" ,"Firozpur" ,"Gurdaspur" ,"Hoshiarpur" ,"Jalandhar" ,"Kapurthala" ,"Ludhiana" ,"Malerkotla" ,"Mansa" ,"Moga" ,"Mohali" ,"Muktsar" ,"Pathankot" ,"Patiala" ,"Rupnagar" ,"Sangrur" ,"Shaheed Bhagat Singh Nagar" ,"Tarn Taran"]
    Rajasthan = ['Rajasthan', "Ajmer" ,"Alwar" ,"Banswara" ,"Baran" ,"Barmer" ,"Bharatpur" ,"Bhilwara" ,"Bikaner" ,"Bundi" ,"Chittorgarh" ,"Churu" ,"Dausa" ,"Dholpur" ,"Dungarpur" ,"Hanumangarh" ,"Jaipur" ,"Jaisalmer" ,"Jalore" ,"Jhalawar" ,"Jhunjhunu" ,"Jodhpur" ,"Karauli" ,"Kota" ,"Nagaur" ,"Pali" ,"Pratapgarh" ,"Rajsamand" ,"Sawai Madhopur" ,"Sikar" ,"Sirohi" ,"Sri Ganganagar" ,"Tonk" ,"Udaipur"]
    Sikkim = ['Sikkim','Soreng','Pakyong']
    TamilNadu = ["Tamil Nadu", "Ariyalur" ,"Chengalpattu" ,"Chennai" ,"Coimbatore" ,"Cuddalore" ,"Dharmapuri" ,"Dindigul" ,"Erode" ,"Kallakurichi" ,"Kanchipuram" ,"Kanyakumari" ,"Karur" ,"Krishnagiri" ,"Madurai" ,"Mayiladuthurai" ,"Nagapattinam" ,"Namakkal" ,"Nilgiris" ,"Perambalur" ,"Pudukkottai" ,"Ramanathapuram" ,"Ranipet" ,"Salem" ,"Sivaganga" ,"Tenkasi" ,"Thanjavur" ,"Theni" ,"Thoothukudi" ,"Tiruchirappalli" ,"Tirunelveli" ,"Tirupattur" ,"Tiruppur" ,"Tiruvallur" ,"Tiruvannamalai" ,"Tiruvarur" ,"Vellore" ,"Viluppuram" ,"Virudhunagar"]
    Telangana = ['Telangana',"Adilabad" ,"Bhadradri Kothagudem" ,"Hanamkonda" ,"Hyderabad" ,"Jagtial" ,"Jangaon" ,"Jayashankar" ,"Jogulamba" ,"Kamareddy" ,"Karimnagar" ,"Khammam" ,"Komaram Bheem" ,"Mahabubabad" ,"Mahbubnagar" ,"Mancherial" ,"Medak" ,"Medchal" ,"Mulugu" ,"Nagarkurnool" ,"Nalgonda" ,"Narayanpet" ,"Nirmal" ,"Nizamabad" ,"Peddapalli" ,"Rajanna Sircilla" ,"Ranga Reddy" ,"Sangareddy" ,"Siddipet" ,"Suryapet" ,"Vikarabad" ,"Wanaparthy" ,"Warangal" ,"Yadadri Bhuvanagiri"]
    Tripura = ['Tripura',"Dhalai" ,"Gomati" ,"Khowai" ,"North Tripura" ,"Sepahijala" ,"South Tripura" ,"Unakoti" ,"West Tripura" ]
    Uttarakhand = ['Uttarakhand',"Almora" ,"Bageshwar" ,"Chamoli" ,"Champawat" ,"Dehradun" ,"Haridwar" ,"Nainital" ,"Pauri" ,"Pithoragarh" ,"Rudraprayag" ,"Tehri" ,"Udham Singh Nagar" ,"Uttarkashi"]
    WestBengal = ['Bengal', "Alipurduar" ,"Bankura" ,"Birbhum" ,"Cooch Behar" ,"Dakshin Dinajpur" ,"Darjeeling" ,"Hooghly" ,"Howrah" ,"Jalpaiguri" ,"Jhargram" ,"Kalimpong" ,"Kolkata" ,"Malda" ,"Murshidabad" ,"Nadia" ,"North 24 Parganas" ,"Paschim Bardhaman" ,"Paschim Medinipur" ,"Purba Bardhaman" ,"Purba Medinipur" ,"Purulia" ,"South 24 Parganas" ,"Uttar Dinajpur"]

    data ={
        "States":['Andaman Nicobar', 'Andhra Pradesh', 'Arunachal Pradesh',
         'Assam', 'Bihar', 'Chandigarh',
          'Chhattisgarh', 'Dadra Nagar',
           'Delhi', 'Goa', 'Gujarat', 'Haryana', 'Himachal Pradesh',
            'Jammu Kashmir', 'Jharkhand', 'Karnataka', 'Kerala',
             'Ladakh', 'Lakshadweep', 'Madhya Pradesh', 'Maharashtra',
              'Manipur', 'Meghalaya', 'Mizoram', 'Nagaland', 'Odisha',
               'Puducherry', 'Punjab', 'Rajasthan', 'Sikkim', 'Tamil Nadu'
               , 'Telangana', 'Tripura', 'Uttar Pradesh', 
               'Uttarakhand', 'West Bengal'],
        "Reported":[hd.countOccurancesAny(AndamanNicobar),hd.countOccurancesAny(AndhraPradesh),hd.countOccurancesAny(ArunachalPradesh),
        hd.countOccurancesAny(Assam),hd.countOccurancesAny(Bihar),hd.countOccurancesAny(Chandigarh),
        hd.countOccurancesAny(Chhattisgarh),hd.countOccurancesAny(Dadra),hd.countOccurancesAny(Delhi),
        hd.countOccurancesAny(Goa),hd.countOccurancesAny(Gujrat),hd.countOccurancesAny(Haryana),
        hd.countOccurancesAny(HimachalPradesh),hd.countOccurancesAny(JammuKashmir),hd.countOccurancesAny(Jharkand),
        hd.countOccurancesAny(Karnataka),hd.countOccurancesAny(Kerala),hd.countOccurancesAny(Ladakh),
        hd.countOccurancesAny(Lakshadweep),hd.countOccurancesAny(MadhyaPradesh),hd.countOccurancesAny(Maharashtra),
        hd.countOccurancesAny(Manipur),hd.countOccurancesAny(Meghalaya),
        hd.countOccurancesAny(Mizoram),hd.countOccurancesAny(Nagaland),hd.countOccurancesAny(Odisha),
        hd.countOccurancesAny(Puducherry),hd.countOccurancesAny(Punjab),hd.countOccurancesAny(Rajasthan),
        hd.countOccurancesAny(Sikkim),hd.countOccurancesAny(TamilNadu),hd.countOccurancesAny(Telangana),
        hd.countOccurancesAny(Tripura),hd.countOccurancesAny(UttarPradesh),hd.countOccurancesAny(Uttarakhand),hd.countOccurancesAny(WestBengal)]
    }

    df = pd.DataFrame(data)
    print(df.sort_values("Reported",ascending=False))
    print(df)

#                 States  Reported
#   33      Uttar Pradesh     19712
#   20        Maharashtra     11281
#   8               Delhi      6031
#   13      Jammu Kashmir      5658
#   10            Gujarat      4998
#   12   Himachal Pradesh      4335
#   4               Bihar      3712
#   27             Punjab      3627
#   35        West Bengal      3310
#   19     Madhya Pradesh      2543
#   28          Rajasthan      2293
#   9                 Goa      2170
#   11            Haryana      2123
#   1      Andhra Pradesh      2030
#   16             Kerala      2025
#   6        Chhattisgarh      1860
#   5          Chandigarh      1860
#   15          Karnataka      1812
#   30         Tamil Nadu      1799
#   3               Assam      1637
#   25             Odisha      1484
#   31          Telangana      1285
#   17             Ladakh      1158
#   7         Dadra Nagar       587
#   21            Manipur       575
#   34        Uttarakhand       563
#   22          Meghalaya       409
#   2   Arunachal Pradesh       394
#   14          Jharkhand       340
#   26         Puducherry       307
#   32            Tripura       199
#   24           Nagaland       185
#   29             Sikkim       160
#   23            Mizoram       144
#   0     Andaman Nicobar       102
#   18        Lakshadweep        29

# Most Criminal State
# Mostly true to crime rates observed, but southern states are under reported by journalists. Please research on your own.

if False:

    UttarPradesh = ['Uttar Pradesh', ' UP ',"Agra" ,"Aligarh" ,"Ambedkar Nagar" ,"Amethi" ,"Amroha" ,"Auraiya" ,"Ayodhya" ,"Azamgarh" ,"Baghpat" ,"Bahraich" ,"Ballia" ,"Balrampur" ,"Barabanki" ,"Bareilly" ,"Bhadohi" ,"Bijnor" ,"Budaun" ,"Bulandshahr" ,"Chandauli" ,"Chitrakoot" ,"Deoria" ,"Etah" ,"Etawah" ,"Farrukhabad" ,"Fatehpur" ,"Firozabad" ,"Gautam Buddha Nagar" ,"Ghaziabad" ,"Ghazipur" ,"Gorakhpur" ,"Hamirpur" ,"Hardoi" ,"Hathras" ,"Jalaun" ,"Jaunpur" ,"Jhansi" ,"Kannauj" ,"Kanpur Dehat" ,"Kanpur Nagar" ,"Kasganj" ,"Kaushambi" ,"Kushinagar" ,"Lalitpur" ,"Lucknow" ,"Maharajganj" ,"Mahoba" ,"Mainpuri" ,"Mathura" ,"Meerut" ,"Mirzapur" ,"Moradabad" ,"Muzaffarnagar" ,"Pilibhit" ,"Pratapgarh" ,"Prayagraj" ,"Raebareli" ,"Rampur" ,"Saharanpur" ,"Sambhal" ,"Sant Kabir Nagar" ,"Shahjahanpur" ,"Shamli" ,"Shravasti" ,"Siddharthnagar" ,"Sitapur" ,"Sonbhadra" ,"Sultanpur" ,"Unnao" ,"Varanasi" ]
    AndamanNicobar = ["Andaman","Nicobar"]
    AndhraPradesh = ["Andhra","Anantapur" ,"Chittoor" ,"East Godavari" ,"Alluri Sitarama Raju" ,"Anakapalli" ,"Annamaya" ,"Bapatla" ,"Eluru" ,"Guntur" ,"Kadapa" ,"Kakinada" ,"Konaseema" ,"Krishna" ,"Kurnool" ,"Manyam" ,"N T Rama Rao" ,"Nandyal" ,"Nellore" ,"Palnadu" ,"Prakasam" ,"Sri Balaji" ,"Sri Satya Sai" ,"Srikakulam" ,"Visakhapatnam" ,"Vizianagaram" ,"West Godavari"]
    ArunachalPradesh = ['Arunachal',"Anjaw" ,"Changlang" ,"Dibang Valley" ,"East Kameng" ,"East Siang" ,"Kamle" ,"Kra Daadi" ,"Kurung Kumey" ,"Lepa Rada" ,"Lohit" ,"Longding" ,"Lower Dibang Valley" ,"Lower Siang" ,"Lower Subansiri" ,"Namsai" ,"Pakke Kessang" ,"Papum Pare" ,"Shi Yomi" ,"Siang" ,"Tawang" ,"Tirap" ,"Upper Siang" ,"Upper Subansiri" ,"West Kameng" ,"West Siang" ]
    Assam = ['assam',"Bajali" ,"Baksa" ,"Barpeta" ,"Biswanath" ,"Bongaigaon" ,"Cachar" ,"Charaideo" ,"Chirang" ,"Darrang" ,"Dhemaji" ,"Dhubri" ,"Dibrugarh" ,"Dima Hasao" ,"Goalpara" ,"Golaghat" ,"Hailakandi" ,"Hojai" ,"Jorhat" ,"Kamrup" ,"Kamrup Metropolitan" ,"Karbi Anglong" ,"Karimganj" ,"Kokrajhar" ,"Lakhimpur" ,"Majuli" ,"Morigaon" ,"Nagaon" ,"Nalbari" ,"Sivasagar" ,"Sonitpur" ,"South Salmara-Mankachar" ,"Tinsukia" ,"Udalguri" ,"West Karbi Anglong" ]    
    Bihar = ['bihar', "Araria" ,"Arwal" ,"Aurangabad" ,"Banka" ,"Begusarai" ,"Bhagalpur" ,"Bhojpur" ,"Buxar" ,"Darbhanga" ,"East Champaran" ,"Gaya" ,"Gopalganj" ,"Jamui" ,"Jehanabad" ,"Kaimur" ,"Katihar" ,"Khagaria" ,"Kishanganj" ,"Lakhisarai" ,"Madhepura" ,"Madhubani" ,"Munger" ,"Muzaffarpur" ,"Nalanda" ,"Nawada" ,"Patna" ,"Purnia" ,"Rohtas" ,"Saharsa" ,"Samastipur" ,"Saran" ,"Sheikhpura" ,"Sheohar" ,"Sitamarhi" ,"Siwan" ,"Supaul" ,"Vaishali" ,"West Champaran"]
    Chandigarh = ['Chandigarh']
    Chhattisgarh = ['Chhattisgarh', "Balod" ,"Baloda Bazar" ,"Balrampur" ,"Bastar" ,"Bemetara" ,"Bijapur" ,"Bilaspur" ,"Dantewada" ,"Dhamtari" ,"Durg" ,"Gariaband" ,"Gaurela Pendra Marwahi" ,"Janjgir Champa" ,"Jashpur" ,"Kabirdham" ,"Kanker" ,"Kondagaon" ,"Korba" ,"Koriya" ,"Mahasamund" ,"Manendragarh" ,"Mohla Manpur" ,"Mungeli" ,"Narayanpur" ,"Raigarh" ,"Raipur" ,"Rajnandgaon" ,"Sakti" ,"Sarangarh Bilaigarh" ,"Sukma" ,"Surajpur"]
    Dadra = ['Dadra', 'Daman', 'Diu']
    Delhi = ['Delhi']
    Goa = ['Goa']
    Gujrat = ['Gujrat', "Ahmedabad" ,"Amreli" ,"Anand" ,"Aravalli" ,"Banaskantha" ,"Bharuch" ,"Bhavnagar" ,"Botad" ,"Chhota Udaipur" ,"Dahod" ,"Dang" ,"Devbhoomi Dwarka" ,"Gandhinagar" ,"Gir Somnath" ,"Jamnagar" ,"Junagadh" ,"Kheda" ,"Kutch" ,"Mahisagar" ,"Mehsana" ,"Morbi" ,"Narmada" ,"Navsari" ,"Panchmahal" ,"Patan" ,"Porbandar" ,"Rajkot" ,"Sabarkantha" ,"Surat" ,"Surendranagar" ,"Tapi" ,"Vadodara" ,"Valsad"]
    Haryana = ['Haryana', "Ambala" ,"Bhiwani" ,"Charkhi Dadri" ,"Faridabad" ,"Fatehabad" ,"Gurugram" ,"Hisar" ,"Jhajjar" ,"Jind" ,"Kaithal" ,"Karnal" ,"Kurukshetra" ,"Mahendragarh" ,"Mewat" ,"Palwal" ,"Panchkula" ,"Panipat" ,"Rewari" ,"Rohtak" ,"Sirsa" ,"Sonipat" ,"Yamunanagar"]
    HimachalPradesh = ['Himachal',"Bilaspur" ,"Chamba" ,"Hamirpur" ,"Kangra" ,"Kinnaur" ,"Kullu" ,"Lahaul Spiti" ,"Mandi" ,"Shimla" ,"Sirmaur" ,"Solan" ,"Una" ]
    JammuKashmir = ["Jammu", "Kashmir", "J&K", "JK", "Anantnag" ,"Bandipora" ,"Baramulla" ,"Budgam" ,"Doda" ,"Ganderbal" ,"Jammu" ,"Kathua" ,"Kishtwar" ,"Kulgam" ,"Kupwara" ,"Poonch" ,"Pulwama" ,"Rajouri" ,"Ramban" ,"Reasi" ,"Samba" ,"Shopian" ,"Srinagar" ,"Udhampur"]
    Jharkand = ["Jharkand", "Bokaro" ,"Chatra" ,"Deoghar" ,"Dhanbad" ,"Dumka" ,"East Singhbhum" ,"Garhwa" ,"Giridih" ,"Godda" ,"Gumla" ,"Hazaribagh" ,"Jamtara" ,"Khunti" ,"Koderma" ,"Latehar" ,"Lohardaga" ,"Pakur" ,"Palamu" ,"Ramgarh" ,"Ranchi" ,"Sahebganj" ,"Seraikela Kharsawan" ,"Simdega" ,"West Singhbhum"]
    Karnataka = ['Karnataka',"Bagalkot" ,"Bangalore Rural" ,"Bangalore Urban" ,"Belgaum" ,"Bellary" ,"Bidar" ,"Chamarajanagar" ,"Chikkaballapur" ,"Chikkamagaluru" ,"Chitradurga" ,"Dakshina Kannada" ,"Davanagere" ,"Dharwad" ,"Gadag" ,"Gulbarga" ,"Hassan" ,"Haveri" ,"Kodagu" ,"Kolar" ,"Koppal" ,"Mandya" ,"Mysore" ,"Raichur" ,"Ramanagara" ,"Shimoga" ,"Tumkur" ,"Udupi" ,"Uttara Kannada" ,"Vijayanagara" ,"Vijayapura" ,"Yadgir"]
    Kerala = ['Kerala', "Alappuzha" ,"Ernakulam" ,"Idukki" ,"Kannur" ,"Kasaragod" ,"Kollam" ,"Kottayam" ,"Kozhikode" ,"Malappuram" ,"Palakkad" ,"Pathanamthitta" ,"Thiruvananthapuram" ,"Thrissur" ,"Wayanad"]
    Ladakh = ['Ladakh','leh','kargil']
    Lakshadweep = ['Lakshadweep']
    MadhyaPradesh = ["Madhya", "Agar Malwa" ,"Alirajpur" ,"Anuppur" ,"Ashoknagar" ,"Balaghat" ,"Barwani" ,"Betul" ,"Bhind" ,"Bhopal" ,"Burhanpur" ,"Chachaura" ,"Chhatarpur" ,"Chhindwara" ,"Damoh" ,"Datia" ,"Dewas" ,"Dhar" ,"Dindori" ,"Guna" ,"Gwalior" ,"Harda" ,"Hoshangabad" ,"Indore" ,"Jabalpur" ,"Jhabua" ,"Katni" ,"Khandwa" ,"Khargone" ,"Maihar" ,"Mandla" ,"Mandsaur" ,"Morena" ,"Nagda" ,"Narsinghpur" ,"Neemuch" ,"Niwari" ,"Panna" ,"Raisen" ,"Rajgarh" ,"Ratlam" ,"Rewa" ,"Sagar" ,"Satna" ,"Sehore" ,"Seoni" ,"Shahdol" ,"Shajapur" ,"Sheopur" ,"Shivpuri" ,"Sidhi" ,"Singrauli" ,"Tikamgarh" ,"Ujjain" ,"Umaria" ,"Vidisha"]
    Maharashtra = ["Maharashtra", "Bombay", "Ahmednagar" ,"Akola" ,"Amravati" ,"Aurangabad" ,"Beed" ,"Bhandara" ,"Buldhana" ,"Chandrapur" ,"Dhule" ,"Gadchiroli" ,"Gondia" ,"Hingoli" ,"Jalgaon" ,"Jalna" ,"Kolhapur" ,"Latur" ,"Mumbai" ,"Mumbai Suburban" ,"Nagpur" ,"Nanded" ,"Nandurbar" ,"Nashik" ,"Osmanabad" ,"Palghar" ,"Parbhani" ,"Pune" ,"Raigad" ,"Ratnagiri" ,"Sangli" ,"Satara" ,"Sindhudurg" ,"Solapur" ,"Thane" ,"Wardha" ,"Washim" ,"Yavatmal"]
    Manipur = ['Manipur', "Bishnupur" ,"Chandel" ,"Churachandpur" ,"Imphal East" ,"Imphal West" ,"Jiribam" ,"Kakching" ,"Kamjong" ,"Kangpokpi" ,"Noney" ,"Pherzawl" ,"Senapati" ,"Tamenglong" ,"Tengnoupal" ,"Thoubal" ,"Ukhrul"]
    Meghalaya = ['Megh', "East Garo Hills" ,"East Jaintia Hills" ,"East Khasi Hills" ,"Mairang" ,"North Garo Hills" ,"Ri Bhoi" ,"South Garo Hills" ,"South West Garo Hills" ,"South West Khasi Hills" ,"West Garo Hills" ,"West Jaintia Hills" ,"West Khasi Hills"]
    Mizoram = ['Mizoram', "Aizawl" ,"Champhai" ,"Hnahthial" ,"Khawzawl" ,"Kolasib" ,"Lawngtlai" ,"Lunglei" ,"Mamit" ,"Saiha" ,"Saitual" ,"Serchhip" ]
    Nagaland = ['Nagaland', "Chumukedima" ,"Dimapur" ,"Kiphire" ,"Kohima" ,"Longleng" ,"Mokokchung" ,"Niuland" ,"Noklak" ,"Peren" ,"Phek" ,"Tseminyu" ,"Tuensang" ,"Wokha" ,"Zunheboto"]
    Odisha = ['Odisha', "Angul" ,"Balangir" ,"Balasore" ,"Bargarh" ,"Bhadrak" ,"Boudh" ,"Cuttack" ,"Debagarh" ,"Dhenkanal" ,"Gajapati" ,"Ganjam" ,"Jagatsinghpur" ,"Jajpur" ,"Jharsuguda" ,"Kalahandi" ,"Kandhamal" ,"Kendrapara" ,"Kendujhar" ,"Khordha" ,"Koraput" ,"Malkangiri" ,"Mayurbhanj" ,"Nabarangpur" ,"Nayagarh" ,"Nuapada" ,"Puri" ,"Rayagada" ,"Sambalpur" ,"Subarnapur" ,"Sundergarh"]
    Puducherry = ['Puducherry', "Karaikal" ,"Mahe" ,"Puducherry" ,"Yanam" ]
    Punjab = ['Punjab', "Amritsar" ,"Barnala" ,"Bathinda" ,"Faridkot" ,"Fatehgarh Sahib" ,"Fazilka" ,"Firozpur" ,"Gurdaspur" ,"Hoshiarpur" ,"Jalandhar" ,"Kapurthala" ,"Ludhiana" ,"Malerkotla" ,"Mansa" ,"Moga" ,"Mohali" ,"Muktsar" ,"Pathankot" ,"Patiala" ,"Rupnagar" ,"Sangrur" ,"Shaheed Bhagat Singh Nagar" ,"Tarn Taran"]
    Rajasthan = ['Rajasthan', "Ajmer" ,"Alwar" ,"Banswara" ,"Baran" ,"Barmer" ,"Bharatpur" ,"Bhilwara" ,"Bikaner" ,"Bundi" ,"Chittorgarh" ,"Churu" ,"Dausa" ,"Dholpur" ,"Dungarpur" ,"Hanumangarh" ,"Jaipur" ,"Jaisalmer" ,"Jalore" ,"Jhalawar" ,"Jhunjhunu" ,"Jodhpur" ,"Karauli" ,"Kota" ,"Nagaur" ,"Pali" ,"Pratapgarh" ,"Rajsamand" ,"Sawai Madhopur" ,"Sikar" ,"Sirohi" ,"Sri Ganganagar" ,"Tonk" ,"Udaipur"]
    Sikkim = ['Sikkim','Soreng','Pakyong']
    TamilNadu = ["Tamil Nadu", "Ariyalur" ,"Chengalpattu" ,"Chennai" ,"Coimbatore" ,"Cuddalore" ,"Dharmapuri" ,"Dindigul" ,"Erode" ,"Kallakurichi" ,"Kanchipuram" ,"Kanyakumari" ,"Karur" ,"Krishnagiri" ,"Madurai" ,"Mayiladuthurai" ,"Nagapattinam" ,"Namakkal" ,"Nilgiris" ,"Perambalur" ,"Pudukkottai" ,"Ramanathapuram" ,"Ranipet" ,"Salem" ,"Sivaganga" ,"Tenkasi" ,"Thanjavur" ,"Theni" ,"Thoothukudi" ,"Tiruchirappalli" ,"Tirunelveli" ,"Tirupattur" ,"Tiruppur" ,"Tiruvallur" ,"Tiruvannamalai" ,"Tiruvarur" ,"Vellore" ,"Viluppuram" ,"Virudhunagar"]
    Telangana = ['Telangana',"Adilabad" ,"Bhadradri Kothagudem" ,"Hanamkonda" ,"Hyderabad" ,"Jagtial" ,"Jangaon" ,"Jayashankar" ,"Jogulamba" ,"Kamareddy" ,"Karimnagar" ,"Khammam" ,"Komaram Bheem" ,"Mahabubabad" ,"Mahbubnagar" ,"Mancherial" ,"Medak" ,"Medchal" ,"Mulugu" ,"Nagarkurnool" ,"Nalgonda" ,"Narayanpet" ,"Nirmal" ,"Nizamabad" ,"Peddapalli" ,"Rajanna Sircilla" ,"Ranga Reddy" ,"Sangareddy" ,"Siddipet" ,"Suryapet" ,"Vikarabad" ,"Wanaparthy" ,"Warangal" ,"Yadadri Bhuvanagiri"]
    Tripura = ['Tripura',"Dhalai" ,"Gomati" ,"Khowai" ,"North Tripura" ,"Sepahijala" ,"South Tripura" ,"Unakoti" ,"West Tripura" ]
    Uttarakhand = ['Uttarakhand',"Almora" ,"Bageshwar" ,"Chamoli" ,"Champawat" ,"Dehradun" ,"Haridwar" ,"Nainital" ,"Pauri" ,"Pithoragarh" ,"Rudraprayag" ,"Tehri" ,"Udham Singh Nagar" ,"Uttarkashi"]
    WestBengal = ['Bengal', "Alipurduar" ,"Bankura" ,"Birbhum" ,"Cooch Behar" ,"Dakshin Dinajpur" ,"Darjeeling" ,"Hooghly" ,"Howrah" ,"Jalpaiguri" ,"Jhargram" ,"Kalimpong" ,"Kolkata" ,"Malda" ,"Murshidabad" ,"Nadia" ,"North 24 Parganas" ,"Paschim Bardhaman" ,"Paschim Medinipur" ,"Purba Bardhaman" ,"Purba Medinipur" ,"Purulia" ,"South 24 Parganas" ,"Uttar Dinajpur"]

    robbery = ['robbery','thief','thieves','chori']
    sexual = ['rape','rapist','sexual assault']
    dowry = ['dowry','dahej']
    drugs = ['drug']
    traffick = ['traffick']
    cyber = ['hack','cyber crime','phish']
    murder = ['murder']

    crimeMerged = robbery + sexual + dowry + drugs + traffick + cyber + murder

    data ={
        "States":['Andaman Nicobar', 'Andhra Pradesh', 'Arunachal Pradesh',
         'Assam', 'Bihar', 'Chandigarh',
          'Chhattisgarh', 'Dadra Nagar',
           'Delhi', 'Goa', 'Gujarat', 'Haryana', 'Himachal Pradesh',
            'Jammu Kashmir', 'Jharkhand', 'Karnataka', 'Kerala',
             'Ladakh', 'Lakshadweep', 'Madhya Pradesh', 'Maharashtra',
              'Manipur', 'Meghalaya', 'Mizoram', 'Nagaland', 'Odisha',
               'Puducherry', 'Punjab', 'Rajasthan', 'Sikkim', 'Tamil Nadu'
               , 'Telangana', 'Tripura', 'Uttar Pradesh', 
               'Uttarakhand', 'West Bengal'],
        "Reported":[hd.countOccurancesGroupedAny([AndamanNicobar,crimeMerged]),hd.countOccurancesGroupedAny([AndhraPradesh,crimeMerged]),hd.countOccurancesGroupedAny([ArunachalPradesh,crimeMerged]),
        hd.countOccurancesGroupedAny([Assam,crimeMerged]),hd.countOccurancesGroupedAny([Bihar,crimeMerged]),hd.countOccurancesGroupedAny([Chandigarh,crimeMerged]),
        hd.countOccurancesGroupedAny([Chhattisgarh,crimeMerged]),hd.countOccurancesGroupedAny([Dadra,crimeMerged]),hd.countOccurancesGroupedAny([Delhi,crimeMerged]),
        hd.countOccurancesGroupedAny([Goa,crimeMerged]),hd.countOccurancesGroupedAny([Gujrat,crimeMerged]),hd.countOccurancesGroupedAny([Haryana,crimeMerged]),
        hd.countOccurancesGroupedAny([HimachalPradesh,crimeMerged]),hd.countOccurancesGroupedAny([JammuKashmir,crimeMerged]),hd.countOccurancesGroupedAny([Jharkand,crimeMerged]),
        hd.countOccurancesGroupedAny([Karnataka,crimeMerged]),hd.countOccurancesGroupedAny([Kerala,crimeMerged]),hd.countOccurancesGroupedAny([Ladakh,crimeMerged]),
        hd.countOccurancesGroupedAny([Lakshadweep,crimeMerged]),hd.countOccurancesGroupedAny([MadhyaPradesh,crimeMerged]),hd.countOccurancesGroupedAny([Maharashtra,crimeMerged]),
        hd.countOccurancesGroupedAny([Manipur,crimeMerged]),hd.countOccurancesGroupedAny([Meghalaya,crimeMerged]),
        hd.countOccurancesGroupedAny([Mizoram,crimeMerged]),hd.countOccurancesGroupedAny([Nagaland,crimeMerged]),hd.countOccurancesGroupedAny([Odisha,crimeMerged]),
        hd.countOccurancesGroupedAny([Puducherry,crimeMerged]),hd.countOccurancesGroupedAny([Punjab,crimeMerged]),hd.countOccurancesGroupedAny([Rajasthan,crimeMerged]),
        hd.countOccurancesGroupedAny([Sikkim,crimeMerged]),hd.countOccurancesGroupedAny([TamilNadu,crimeMerged]),hd.countOccurancesGroupedAny([Telangana,crimeMerged]),
        hd.countOccurancesGroupedAny([Tripura,crimeMerged]),hd.countOccurancesGroupedAny([UttarPradesh,crimeMerged]),hd.countOccurancesGroupedAny([Uttarakhand,crimeMerged]),hd.countOccurancesGroupedAny([WestBengal,crimeMerged])]
    }

    df = pd.DataFrame(data)
    print(df.sort_values("Reported",ascending=False))

#                  States  Reported
#   34        Uttarakhand       7
#   20        Maharashtra       270
#   33      Uttar Pradesh       261
#   8               Delhi       183
#   4               Bihar       113
#   11            Haryana        87
#   9                 Goa        86
#   10            Gujarat        80
#   28          Rajasthan        76
#   27             Punjab        75
#   12   Himachal Pradesh        67
#   13      Jammu Kashmir        66
#   35        West Bengal        53
#   16             Kerala        52
#   25             Odisha        48
#   19     Madhya Pradesh        40
#   3               Assam        34
#   1      Andhra Pradesh        32
#   30         Tamil Nadu        25
#   15          Karnataka        23
#   14          Jharkhand        19
#   21            Manipur        15
#   31          Telangana        12
#   6        Chhattisgarh        11
#   22          Meghalaya         7
#   32            Tripura         5
#   5          Chandigarh         4
#   7         Dadra Nagar         3
#   2   Arunachal Pradesh         3
#   0     Andaman Nicobar         2
#   29             Sikkim         2
#   23            Mizoram         2
#   17             Ladakh         2
#   26         Puducherry         1
#   24           Nagaland         1
#   18        Lakshadweep         0

# Most Crime/State by specific crime

if False:

    UttarPradesh = ['Uttar Pradesh', ' UP ',"Agra" ,"Aligarh" ,"Ambedkar Nagar" ,"Amethi" ,"Amroha" ,"Auraiya" ,"Ayodhya" ,"Azamgarh" ,"Baghpat" ,"Bahraich" ,"Ballia" ,"Balrampur" ,"Barabanki" ,"Bareilly" ,"Bhadohi" ,"Bijnor" ,"Budaun" ,"Bulandshahr" ,"Chandauli" ,"Chitrakoot" ,"Deoria" ,"Etah" ,"Etawah" ,"Farrukhabad" ,"Fatehpur" ,"Firozabad" ,"Gautam Buddha Nagar" ,"Ghaziabad" ,"Ghazipur" ,"Gorakhpur" ,"Hamirpur" ,"Hardoi" ,"Hathras" ,"Jalaun" ,"Jaunpur" ,"Jhansi" ,"Kannauj" ,"Kanpur Dehat" ,"Kanpur Nagar" ,"Kasganj" ,"Kaushambi" ,"Kushinagar" ,"Lalitpur" ,"Lucknow" ,"Maharajganj" ,"Mahoba" ,"Mainpuri" ,"Mathura" ,"Meerut" ,"Mirzapur" ,"Moradabad" ,"Muzaffarnagar" ,"Pilibhit" ,"Pratapgarh" ,"Prayagraj" ,"Raebareli" ,"Rampur" ,"Saharanpur" ,"Sambhal" ,"Sant Kabir Nagar" ,"Shahjahanpur" ,"Shamli" ,"Shravasti" ,"Siddharthnagar" ,"Sitapur" ,"Sonbhadra" ,"Sultanpur" ,"Unnao" ,"Varanasi" ]
    AndamanNicobar = ["Andaman","Nicobar"]
    AndhraPradesh = ["Andhra","Anantapur" ,"Chittoor" ,"East Godavari" ,"Alluri Sitarama Raju" ,"Anakapalli" ,"Annamaya" ,"Bapatla" ,"Eluru" ,"Guntur" ,"Kadapa" ,"Kakinada" ,"Konaseema" ,"Krishna" ,"Kurnool" ,"Manyam" ,"N T Rama Rao" ,"Nandyal" ,"Nellore" ,"Palnadu" ,"Prakasam" ,"Sri Balaji" ,"Sri Satya Sai" ,"Srikakulam" ,"Visakhapatnam" ,"Vizianagaram" ,"West Godavari"]
    ArunachalPradesh = ['Arunachal',"Anjaw" ,"Changlang" ,"Dibang Valley" ,"East Kameng" ,"East Siang" ,"Kamle" ,"Kra Daadi" ,"Kurung Kumey" ,"Lepa Rada" ,"Lohit" ,"Longding" ,"Lower Dibang Valley" ,"Lower Siang" ,"Lower Subansiri" ,"Namsai" ,"Pakke Kessang" ,"Papum Pare" ,"Shi Yomi" ,"Siang" ,"Tawang" ,"Tirap" ,"Upper Siang" ,"Upper Subansiri" ,"West Kameng" ,"West Siang" ]
    Assam = ['assam',"Bajali" ,"Baksa" ,"Barpeta" ,"Biswanath" ,"Bongaigaon" ,"Cachar" ,"Charaideo" ,"Chirang" ,"Darrang" ,"Dhemaji" ,"Dhubri" ,"Dibrugarh" ,"Dima Hasao" ,"Goalpara" ,"Golaghat" ,"Hailakandi" ,"Hojai" ,"Jorhat" ,"Kamrup" ,"Kamrup Metropolitan" ,"Karbi Anglong" ,"Karimganj" ,"Kokrajhar" ,"Lakhimpur" ,"Majuli" ,"Morigaon" ,"Nagaon" ,"Nalbari" ,"Sivasagar" ,"Sonitpur" ,"South Salmara-Mankachar" ,"Tinsukia" ,"Udalguri" ,"West Karbi Anglong" ]    
    Bihar = ['bihar', "Araria" ,"Arwal" ,"Aurangabad" ,"Banka" ,"Begusarai" ,"Bhagalpur" ,"Bhojpur" ,"Buxar" ,"Darbhanga" ,"East Champaran" ,"Gaya" ,"Gopalganj" ,"Jamui" ,"Jehanabad" ,"Kaimur" ,"Katihar" ,"Khagaria" ,"Kishanganj" ,"Lakhisarai" ,"Madhepura" ,"Madhubani" ,"Munger" ,"Muzaffarpur" ,"Nalanda" ,"Nawada" ,"Patna" ,"Purnia" ,"Rohtas" ,"Saharsa" ,"Samastipur" ,"Saran" ,"Sheikhpura" ,"Sheohar" ,"Sitamarhi" ,"Siwan" ,"Supaul" ,"Vaishali" ,"West Champaran"]
    Chandigarh = ['Chandigarh']
    Chhattisgarh = ['Chhattisgarh', "Balod" ,"Baloda Bazar" ,"Balrampur" ,"Bastar" ,"Bemetara" ,"Bijapur" ,"Bilaspur" ,"Dantewada" ,"Dhamtari" ,"Durg" ,"Gariaband" ,"Gaurela Pendra Marwahi" ,"Janjgir Champa" ,"Jashpur" ,"Kabirdham" ,"Kanker" ,"Kondagaon" ,"Korba" ,"Koriya" ,"Mahasamund" ,"Manendragarh" ,"Mohla Manpur" ,"Mungeli" ,"Narayanpur" ,"Raigarh" ,"Raipur" ,"Rajnandgaon" ,"Sakti" ,"Sarangarh Bilaigarh" ,"Sukma" ,"Surajpur"]
    Dadra = ['Dadra', 'Daman', 'Diu']
    Delhi = ['Delhi']
    Goa = ['Goa']
    Gujrat = ['Gujrat', "Ahmedabad" ,"Amreli" ,"Anand" ,"Aravalli" ,"Banaskantha" ,"Bharuch" ,"Bhavnagar" ,"Botad" ,"Chhota Udaipur" ,"Dahod" ,"Dang" ,"Devbhoomi Dwarka" ,"Gandhinagar" ,"Gir Somnath" ,"Jamnagar" ,"Junagadh" ,"Kheda" ,"Kutch" ,"Mahisagar" ,"Mehsana" ,"Morbi" ,"Narmada" ,"Navsari" ,"Panchmahal" ,"Patan" ,"Porbandar" ,"Rajkot" ,"Sabarkantha" ,"Surat" ,"Surendranagar" ,"Tapi" ,"Vadodara" ,"Valsad"]
    Haryana = ['Haryana', "Ambala" ,"Bhiwani" ,"Charkhi Dadri" ,"Faridabad" ,"Fatehabad" ,"Gurugram" ,"Hisar" ,"Jhajjar" ,"Jind" ,"Kaithal" ,"Karnal" ,"Kurukshetra" ,"Mahendragarh" ,"Mewat" ,"Palwal" ,"Panchkula" ,"Panipat" ,"Rewari" ,"Rohtak" ,"Sirsa" ,"Sonipat" ,"Yamunanagar"]
    HimachalPradesh = ['Himachal',"Bilaspur" ,"Chamba" ,"Hamirpur" ,"Kangra" ,"Kinnaur" ,"Kullu" ,"Lahaul Spiti" ,"Mandi" ,"Shimla" ,"Sirmaur" ,"Solan" ,"Una" ]
    JammuKashmir = ["Jammu", "Kashmir", "J&K", "JK", "Anantnag" ,"Bandipora" ,"Baramulla" ,"Budgam" ,"Doda" ,"Ganderbal" ,"Jammu" ,"Kathua" ,"Kishtwar" ,"Kulgam" ,"Kupwara" ,"Poonch" ,"Pulwama" ,"Rajouri" ,"Ramban" ,"Reasi" ,"Samba" ,"Shopian" ,"Srinagar" ,"Udhampur"]
    Jharkand = ["Jharkand", "Bokaro" ,"Chatra" ,"Deoghar" ,"Dhanbad" ,"Dumka" ,"East Singhbhum" ,"Garhwa" ,"Giridih" ,"Godda" ,"Gumla" ,"Hazaribagh" ,"Jamtara" ,"Khunti" ,"Koderma" ,"Latehar" ,"Lohardaga" ,"Pakur" ,"Palamu" ,"Ramgarh" ,"Ranchi" ,"Sahebganj" ,"Seraikela Kharsawan" ,"Simdega" ,"West Singhbhum"]
    Karnataka = ['Karnataka',"Bagalkot" ,"Bangalore Rural" ,"Bangalore Urban" ,"Belgaum" ,"Bellary" ,"Bidar" ,"Chamarajanagar" ,"Chikkaballapur" ,"Chikkamagaluru" ,"Chitradurga" ,"Dakshina Kannada" ,"Davanagere" ,"Dharwad" ,"Gadag" ,"Gulbarga" ,"Hassan" ,"Haveri" ,"Kodagu" ,"Kolar" ,"Koppal" ,"Mandya" ,"Mysore" ,"Raichur" ,"Ramanagara" ,"Shimoga" ,"Tumkur" ,"Udupi" ,"Uttara Kannada" ,"Vijayanagara" ,"Vijayapura" ,"Yadgir"]
    Kerala = ['Kerala', "Alappuzha" ,"Ernakulam" ,"Idukki" ,"Kannur" ,"Kasaragod" ,"Kollam" ,"Kottayam" ,"Kozhikode" ,"Malappuram" ,"Palakkad" ,"Pathanamthitta" ,"Thiruvananthapuram" ,"Thrissur" ,"Wayanad"]
    Ladakh = ['Ladakh','leh','kargil']
    Lakshadweep = ['Lakshadweep']
    MadhyaPradesh = ["Madhya", "Agar Malwa" ,"Alirajpur" ,"Anuppur" ,"Ashoknagar" ,"Balaghat" ,"Barwani" ,"Betul" ,"Bhind" ,"Bhopal" ,"Burhanpur" ,"Chachaura" ,"Chhatarpur" ,"Chhindwara" ,"Damoh" ,"Datia" ,"Dewas" ,"Dhar" ,"Dindori" ,"Guna" ,"Gwalior" ,"Harda" ,"Hoshangabad" ,"Indore" ,"Jabalpur" ,"Jhabua" ,"Katni" ,"Khandwa" ,"Khargone" ,"Maihar" ,"Mandla" ,"Mandsaur" ,"Morena" ,"Nagda" ,"Narsinghpur" ,"Neemuch" ,"Niwari" ,"Panna" ,"Raisen" ,"Rajgarh" ,"Ratlam" ,"Rewa" ,"Sagar" ,"Satna" ,"Sehore" ,"Seoni" ,"Shahdol" ,"Shajapur" ,"Sheopur" ,"Shivpuri" ,"Sidhi" ,"Singrauli" ,"Tikamgarh" ,"Ujjain" ,"Umaria" ,"Vidisha"]
    Maharashtra = ["Maharashtra", "Bombay", "Ahmednagar" ,"Akola" ,"Amravati" ,"Aurangabad" ,"Beed" ,"Bhandara" ,"Buldhana" ,"Chandrapur" ,"Dhule" ,"Gadchiroli" ,"Gondia" ,"Hingoli" ,"Jalgaon" ,"Jalna" ,"Kolhapur" ,"Latur" ,"Mumbai" ,"Mumbai Suburban" ,"Nagpur" ,"Nanded" ,"Nandurbar" ,"Nashik" ,"Osmanabad" ,"Palghar" ,"Parbhani" ,"Pune" ,"Raigad" ,"Ratnagiri" ,"Sangli" ,"Satara" ,"Sindhudurg" ,"Solapur" ,"Thane" ,"Wardha" ,"Washim" ,"Yavatmal"]
    Manipur = ['Manipur', "Bishnupur" ,"Chandel" ,"Churachandpur" ,"Imphal East" ,"Imphal West" ,"Jiribam" ,"Kakching" ,"Kamjong" ,"Kangpokpi" ,"Noney" ,"Pherzawl" ,"Senapati" ,"Tamenglong" ,"Tengnoupal" ,"Thoubal" ,"Ukhrul"]
    Meghalaya = ['Megh', "East Garo Hills" ,"East Jaintia Hills" ,"East Khasi Hills" ,"Mairang" ,"North Garo Hills" ,"Ri Bhoi" ,"South Garo Hills" ,"South West Garo Hills" ,"South West Khasi Hills" ,"West Garo Hills" ,"West Jaintia Hills" ,"West Khasi Hills"]
    Mizoram = ['Mizoram', "Aizawl" ,"Champhai" ,"Hnahthial" ,"Khawzawl" ,"Kolasib" ,"Lawngtlai" ,"Lunglei" ,"Mamit" ,"Saiha" ,"Saitual" ,"Serchhip" ]
    Nagaland = ['Nagaland', "Chumukedima" ,"Dimapur" ,"Kiphire" ,"Kohima" ,"Longleng" ,"Mokokchung" ,"Niuland" ,"Noklak" ,"Peren" ,"Phek" ,"Tseminyu" ,"Tuensang" ,"Wokha" ,"Zunheboto"]
    Odisha = ['Odisha', "Angul" ,"Balangir" ,"Balasore" ,"Bargarh" ,"Bhadrak" ,"Boudh" ,"Cuttack" ,"Debagarh" ,"Dhenkanal" ,"Gajapati" ,"Ganjam" ,"Jagatsinghpur" ,"Jajpur" ,"Jharsuguda" ,"Kalahandi" ,"Kandhamal" ,"Kendrapara" ,"Kendujhar" ,"Khordha" ,"Koraput" ,"Malkangiri" ,"Mayurbhanj" ,"Nabarangpur" ,"Nayagarh" ,"Nuapada" ,"Puri" ,"Rayagada" ,"Sambalpur" ,"Subarnapur" ,"Sundergarh"]
    Puducherry = ['Puducherry', "Karaikal" ,"Mahe" ,"Puducherry" ,"Yanam" ]
    Punjab = ['Punjab', "Amritsar" ,"Barnala" ,"Bathinda" ,"Faridkot" ,"Fatehgarh Sahib" ,"Fazilka" ,"Firozpur" ,"Gurdaspur" ,"Hoshiarpur" ,"Jalandhar" ,"Kapurthala" ,"Ludhiana" ,"Malerkotla" ,"Mansa" ,"Moga" ,"Mohali" ,"Muktsar" ,"Pathankot" ,"Patiala" ,"Rupnagar" ,"Sangrur" ,"Shaheed Bhagat Singh Nagar" ,"Tarn Taran"]
    Rajasthan = ['Rajasthan', "Ajmer" ,"Alwar" ,"Banswara" ,"Baran" ,"Barmer" ,"Bharatpur" ,"Bhilwara" ,"Bikaner" ,"Bundi" ,"Chittorgarh" ,"Churu" ,"Dausa" ,"Dholpur" ,"Dungarpur" ,"Hanumangarh" ,"Jaipur" ,"Jaisalmer" ,"Jalore" ,"Jhalawar" ,"Jhunjhunu" ,"Jodhpur" ,"Karauli" ,"Kota" ,"Nagaur" ,"Pali" ,"Pratapgarh" ,"Rajsamand" ,"Sawai Madhopur" ,"Sikar" ,"Sirohi" ,"Sri Ganganagar" ,"Tonk" ,"Udaipur"]
    Sikkim = ['Sikkim','Soreng','Pakyong']
    TamilNadu = ["Tamil Nadu", "Ariyalur" ,"Chengalpattu" ,"Chennai" ,"Coimbatore" ,"Cuddalore" ,"Dharmapuri" ,"Dindigul" ,"Erode" ,"Kallakurichi" ,"Kanchipuram" ,"Kanyakumari" ,"Karur" ,"Krishnagiri" ,"Madurai" ,"Mayiladuthurai" ,"Nagapattinam" ,"Namakkal" ,"Nilgiris" ,"Perambalur" ,"Pudukkottai" ,"Ramanathapuram" ,"Ranipet" ,"Salem" ,"Sivaganga" ,"Tenkasi" ,"Thanjavur" ,"Theni" ,"Thoothukudi" ,"Tiruchirappalli" ,"Tirunelveli" ,"Tirupattur" ,"Tiruppur" ,"Tiruvallur" ,"Tiruvannamalai" ,"Tiruvarur" ,"Vellore" ,"Viluppuram" ,"Virudhunagar"]
    Telangana = ['Telangana',"Adilabad" ,"Bhadradri Kothagudem" ,"Hanamkonda" ,"Hyderabad" ,"Jagtial" ,"Jangaon" ,"Jayashankar" ,"Jogulamba" ,"Kamareddy" ,"Karimnagar" ,"Khammam" ,"Komaram Bheem" ,"Mahabubabad" ,"Mahbubnagar" ,"Mancherial" ,"Medak" ,"Medchal" ,"Mulugu" ,"Nagarkurnool" ,"Nalgonda" ,"Narayanpet" ,"Nirmal" ,"Nizamabad" ,"Peddapalli" ,"Rajanna Sircilla" ,"Ranga Reddy" ,"Sangareddy" ,"Siddipet" ,"Suryapet" ,"Vikarabad" ,"Wanaparthy" ,"Warangal" ,"Yadadri Bhuvanagiri"]
    Tripura = ['Tripura',"Dhalai" ,"Gomati" ,"Khowai" ,"North Tripura" ,"Sepahijala" ,"South Tripura" ,"Unakoti" ,"West Tripura" ]
    Uttarakhand = ['Uttarakhand',"Almora" ,"Bageshwar" ,"Chamoli" ,"Champawat" ,"Dehradun" ,"Haridwar" ,"Nainital" ,"Pithoragarh" ,"Rudraprayag" ,"Udham Singh Nagar" ,"Uttarkashi"]
    WestBengal = ['Bengal', "Alipurduar" ,"Bankura" ,"Birbhum" ,"Cooch Behar" ,"Dakshin Dinajpur" ,"Darjeeling" ,"Hooghly" ,"Howrah" ,"Jalpaiguri" ,"Jhargram" ,"Kalimpong" ,"Kolkata" ,"Malda" ,"Murshidabad" ,"Nadia" ,"North 24 Parganas" ,"Paschim Bardhaman" ,"Paschim Medinipur" ,"Purba Bardhaman" ,"Purba Medinipur" ,"Purulia" ,"South 24 Parganas" ,"Uttar Dinajpur"]

    robbery = ['robbery','thief','thieves','chori']
    sexual = ['rape','rapist','sexual assault']
    dowry = ['dowry','dahej']
    drugs = ['drug']
    traffick = ['traffick']
    cyber = ['hack','cyber crime','phish']
    murder = ['murder']

    crimeMerged =  murder

    data ={
        "States":['Andaman Nicobar', 'Andhra Pradesh', 'Arunachal Pradesh',
         'Assam', 'Bihar', 'Chandigarh',
          'Chhattisgarh', 'Dadra Nagar',
           'Delhi', 'Goa', 'Gujarat', 'Haryana', 'Himachal Pradesh',
            'Jammu Kashmir', 'Jharkhand', 'Karnataka', 'Kerala',
             'Ladakh', 'Lakshadweep', 'Madhya Pradesh', 'Maharashtra',
              'Manipur', 'Meghalaya', 'Mizoram', 'Nagaland', 'Odisha',
               'Puducherry', 'Punjab', 'Rajasthan', 'Sikkim', 'Tamil Nadu'
               , 'Telangana', 'Tripura', 'Uttar Pradesh', 
               'Uttarakhand', 'West Bengal'],
        "Reported":[hd.countOccurancesGroupedAny([AndamanNicobar,crimeMerged]),hd.countOccurancesGroupedAny([AndhraPradesh,crimeMerged]),hd.countOccurancesGroupedAny([ArunachalPradesh,crimeMerged]),
        hd.countOccurancesGroupedAny([Assam,crimeMerged]),hd.countOccurancesGroupedAny([Bihar,crimeMerged]),hd.countOccurancesGroupedAny([Chandigarh,crimeMerged]),
        hd.countOccurancesGroupedAny([Chhattisgarh,crimeMerged]),hd.countOccurancesGroupedAny([Dadra,crimeMerged]),hd.countOccurancesGroupedAny([Delhi,crimeMerged]),
        hd.countOccurancesGroupedAny([Goa,crimeMerged]),hd.countOccurancesGroupedAny([Gujrat,crimeMerged]),hd.countOccurancesGroupedAny([Haryana,crimeMerged]),
        hd.countOccurancesGroupedAny([HimachalPradesh,crimeMerged]),hd.countOccurancesGroupedAny([JammuKashmir,crimeMerged]),hd.countOccurancesGroupedAny([Jharkand,crimeMerged]),
        hd.countOccurancesGroupedAny([Karnataka,crimeMerged]),hd.countOccurancesGroupedAny([Kerala,crimeMerged]),hd.countOccurancesGroupedAny([Ladakh,crimeMerged]),
        hd.countOccurancesGroupedAny([Lakshadweep,crimeMerged]),hd.countOccurancesGroupedAny([MadhyaPradesh,crimeMerged]),hd.countOccurancesGroupedAny([Maharashtra,crimeMerged]),
        hd.countOccurancesGroupedAny([Manipur,crimeMerged]),hd.countOccurancesGroupedAny([Meghalaya,crimeMerged]),
        hd.countOccurancesGroupedAny([Mizoram,crimeMerged]),hd.countOccurancesGroupedAny([Nagaland,crimeMerged]),hd.countOccurancesGroupedAny([Odisha,crimeMerged]),
        hd.countOccurancesGroupedAny([Puducherry,crimeMerged]),hd.countOccurancesGroupedAny([Punjab,crimeMerged]),hd.countOccurancesGroupedAny([Rajasthan,crimeMerged]),
        hd.countOccurancesGroupedAny([Sikkim,crimeMerged]),hd.countOccurancesGroupedAny([TamilNadu,crimeMerged]),hd.countOccurancesGroupedAny([Telangana,crimeMerged]),
        hd.countOccurancesGroupedAny([Tripura,crimeMerged]),hd.countOccurancesGroupedAny([UttarPradesh,crimeMerged]),hd.countOccurancesGroupedAny([Uttarakhand,crimeMerged]),hd.countOccurancesGroupedAny([WestBengal,crimeMerged])]
    }

    df = pd.DataFrame(data)
    print(df.sort_values("Reported",ascending=False))

# Robbery
#                States  Reported
# 20        Maharashtra         7
# 10            Gujarat         6
# 27             Punjab         5
# 33      Uttar Pradesh         5
# 4               Bihar         4
# 9                 Goa         4
# 28          Rajasthan         3
# 8               Delhi         3
# 11            Haryana         3
# 13      Jammu Kashmir         3
# 25             Odisha         2
# 35        West Bengal         1
# 31          Telangana         1
# 1      Andhra Pradesh         1
# 16             Kerala         1
# 12   Himachal Pradesh         1
# 14          Jharkhand         1
# 5          Chandigarh         1
# 3               Assam         1
# 30         Tamil Nadu         0
# 32            Tripura         0
# 34        Uttarakhand         0
# 26         Puducherry         0
# 0     Andaman Nicobar         0
# 24           Nagaland         0
# 23            Mizoram         0
# 22          Meghalaya         0
# 21            Manipur         0
# 19     Madhya Pradesh         0
# 17             Ladakh         0
# 15          Karnataka         0
# 7         Dadra Nagar         0
# 6        Chhattisgarh         0
# 2   Arunachal Pradesh         0
# 18        Lakshadweep         0

# Sexual
#               States  Reported
# 8               Delhi       127
# 20        Maharashtra       106
# 33      Uttar Pradesh        98
# 11            Haryana        57
# 9                 Goa        42
# 35        West Bengal        35
# 4               Bihar        34
# 28          Rajasthan        33
# 10            Gujarat        33
# 13      Jammu Kashmir        27
# 27             Punjab        22
# 16             Kerala        19
# 25             Odisha        17
# 19     Madhya Pradesh        17
# 12   Himachal Pradesh        12
# 15          Karnataka         9
# 3               Assam         9
# 14          Jharkhand         8
# 32            Tripura         5
# 6        Chhattisgarh         5
# 1      Andhra Pradesh         4
# 22          Meghalaya         4
# 30         Tamil Nadu         3
# 31          Telangana         3
# 34        Uttarakhand         3
# 2   Arunachal Pradesh         2
# 21            Manipur         1
# 24           Nagaland         1
# 26         Puducherry         1
# 29             Sikkim         1
# 0     Andaman Nicobar         0
# 23            Mizoram         0
# 17             Ladakh         0
# 7         Dadra Nagar         0
# 5          Chandigarh         0
# 18        Lakshadweep         0

# Drugs 
#                States  Reported
# 33      Uttar Pradesh        28
# 27             Punjab        21
# 20        Maharashtra        17
# 9                 Goa        13
# 25             Odisha        13
# 13      Jammu Kashmir        12
# 21            Manipur        10
# 12   Himachal Pradesh         8
# 10            Gujarat         7
# 8               Delhi         7
# 11            Haryana         3
# 15          Karnataka         3
# 28          Rajasthan         2
# 6        Chhattisgarh         2
# 3               Assam         2
# 23            Mizoram         2
# 19     Madhya Pradesh         2
# 35        West Bengal         2
# 30         Tamil Nadu         1
# 31          Telangana         1
# 22          Meghalaya         1
# 0     Andaman Nicobar         1
# 7         Dadra Nagar         1
# 2   Arunachal Pradesh         1
# 1      Andhra Pradesh         0
# 17             Ladakh         0
# 24           Nagaland         0
# 16             Kerala         0
# 26         Puducherry         0
# 14          Jharkhand         0
# 29             Sikkim         0
# 5          Chandigarh         0
# 4               Bihar         0
# 32            Tripura         0
# 34        Uttarakhand         0
# 18        Lakshadweep         0

# Cyber 
#     States  Reported
# 20        Maharashtra        57
# 4               Bihar        30
# 33      Uttar Pradesh        28
# 12   Himachal Pradesh        10
# 16             Kerala         9
# 8               Delhi         9
# 15          Karnataka         7
# 1      Andhra Pradesh         6
# 9                 Goa         6
# 13      Jammu Kashmir         6
# 30         Tamil Nadu         5
# 27             Punjab         4
# 10            Gujarat         4
# 3               Assam         4
# 25             Odisha         3
# 31          Telangana         3
# 7         Dadra Nagar         2
# 34        Uttarakhand         2
# 19     Madhya Pradesh         2
# 28          Rajasthan         1
# 0     Andaman Nicobar         1
# 35        West Bengal         1
# 14          Jharkhand         1
# 11            Haryana         1
# 22          Meghalaya         0
# 23            Mizoram         0
# 24           Nagaland         0
# 21            Manipur         0
# 26         Puducherry         0
# 17             Ladakh         0
# 29             Sikkim         0
# 6        Chhattisgarh         0
# 32            Tripura         0
# 5          Chandigarh         0
# 2   Arunachal Pradesh         0
# 18        Lakshadweep         0

#Murder
#              States  Reported
# 20        Maharashtra        95
# 33      Uttar Pradesh        93
# 4               Bihar        47
# 28          Rajasthan        38
# 8               Delhi        35
# 12   Himachal Pradesh        30
# 10            Gujarat        29
# 16             Kerala        22
# 11            Haryana        22
# 13      Jammu Kashmir        22
# 27             Punjab        18
# 9                 Goa        18
# 19     Madhya Pradesh        18
# 3               Assam        17
# 1      Andhra Pradesh        17
# 30         Tamil Nadu        16
# 35        West Bengal        16
# 14          Jharkhand         9
# 25             Odisha         7
# 15          Karnataka         5
# 6        Chhattisgarh         5
# 21            Manipur         4
# 31          Telangana         4
# 5          Chandigarh         3
# 17             Ladakh         2
# 22          Meghalaya         2
# 34        Uttarakhand         2
# 29             Sikkim         1
# 32            Tripura         1
# 0     Andaman Nicobar         0
# 26         Puducherry         0
# 24           Nagaland         0
# 23            Mizoram         0
# 7         Dadra Nagar         0
# 2   Arunachal Pradesh         0
# 18        Lakshadweep         0

# SRK vs Salman vs Amir

if False:
    srk = ["srk","shah rukh"]
    salman = ["salman","sallu"]
    amir = ["aamir",]

    data = {"Actor":["SRK","Salman","Amir"],
    "Reported":[hd.countOccurancesAny(srk),hd.countOccurancesAny(salman),hd.countOccurancesAny(amir)]
    }

    df = pd.DataFrame(data)
    print(df.sort_values("Reported",ascending=False))

#     Actor  Reported
# 1  Salman       335
# 0     SRK       304
# 2    Amir       130
