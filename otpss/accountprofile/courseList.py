listOfprograms = [
      'Bachelor of Accountancy'
    , 'Bachelor of Arts Degree in Economics and Accounting (Revised)'
    , 'Bachelor of Business Administration (Entrepreneurship And Enterprise Development)'
    , 'Bachelor of Business Administration (Logistics And Supply Chain Management)'
    , 'Bachelor of Business Administration (Management)'
    , 'Bachelor of Business Administration (Tourism & Hospitality Management'
    , 'Bachelor of Business Administration in International Business'
    , 'Bachelor of Business Administration in Marketing'
    , 'Bachelor of Finance'
    , 'Bachelor of Information Systems (Business Information Systems)'
    , 'Diploma in Business and Accounting Studies (DABS)'
    , 'Revised Bachelor of Business Administration In Tourism And Hospitality Management'
    , 'Revised Bachelor of Information Systems (Business Information Systems)'
    , 'Bachelor of Education (Early Childhood Development and Education)'
    , 'Bachelor of Education (Educational Management)'
    , 'Bachelor of Education (Lifelong Learning and Community Development)'
    , 'Bachelor of Education (Primary Education)'
    , 'Bachelor of Education (Secondary)'
    , 'Bachelor of Education (Secondary) Humanities'
    , 'Bachelor of Education Degree in Science'
    , 'Bachelor of Education in Counselling'
    , 'Bachelor of Education in Physical Education'
    , 'Bachelor of Education in Secondary Education (Biology, Chemistry, Mathematics, Physics)'
    , 'Bachelor of Education in Special Education'
    , 'Bachelor of Family and Consumer Sciences'
    , 'Diploma in Lifelong Learning and Community Development'
    , 'Diploma in NGO Management'
    , 'Post Graduate Diploma in Education'
    , 'Bachelor of Design (Design and Technology Education)'
    , 'Bachelor of Design (Industrial Design)'
    , 'Bachelor of Engineering (Industrial Engineering)'
    , 'Bachelor of Engineering (Mineral Engineering)'
    , 'Bachelor of Engineering (Mining Engineering)'
    , 'Bachelor of Geomatics'
    , 'Bachelor of Land Management'
    , 'Bachelor of Science Degree in Real Estate'
    , 'Bachelor of Architecture'
    , 'Bachelor of Design'
    , 'Bachelor of Electrical and Electronic Engineering'
    , 'Bachelor of Engineering (Civil)'
    , 'Bachelor of Engineering (Construction Engineering and Management)'
    , 'Bachelor of Engineering (Mechanical Engineering)'
    , 'Bachelor of Science Degree in Urban and Regional Planning'
    , 'Combined Bachelor of Engineering (B-Eng Major)'
    , 'Combined Bachelor of Engineering (B-Eng Minor)'
    , 'Combined Bachelor of Engineering Degree (Major in Mechanical Engineering)'
    , 'Combined Degree (Minor in Mechanical Engineering)'
    , 'Bachelor of Nursing Science'
    , 'Bachelor of Pharmacy (B Pharm)'
    , 'Bachelor of Pharmacy (B. Pharm) Programme'
    , 'Bachelor of Science - Environmental Health (BSc-EH)'
    , 'Bachelor of Science Cytotechnology and Histotechnology Sciences (BSc CHS)'
    , 'Bachelor of Science Medical Laboratory Sciences (BSc MLS)'
    , 'Bachelor of Arts Degree in English'
    , 'Bachelor of Arts, Library and Information Studies (BALIS)'
    , 'Bachelor of Arts (Media Studies)'
    , 'Bachelor of Arts Degree in African Languages and Literature'
    , 'Bachelor of Arts Degree in Archaeology'
    , 'Bachelor of Arts Degree in Chinese Studies'
    , 'Bachelor of Arts Degree in French'
    , 'Bachelor of Arts Degree in History'
    , 'Bachelor of Arts in Humanities'
    , 'Bachelor of Arts in Pastoral Studies'
    , 'Bachelor of Fine Arts (Theatre Studies)'
    , 'Bachelor of Information and Knowledge Management'
    , 'Bachelor of Information Systems (Information Management) (BIS)'
    , 'Bachelor of Media Studies (BMS)'
    , 'Bachelor of Medicine Bachelor of Surgery (MBBS)'
    , 'Bachelor of Science (Biological Sciences)'
    , 'Bachelor of Science (Computer Science)'
    , 'Bachelor of Information Systems (Computer Information Systems)'
    , 'Bachelor of Science (Computing with Finance)'
    , 'Bachelor of Science (Information Technology)'
    , 'Bachelor of Science (Physics)'
    , 'Bachelor of Science Degree in Chemistry'
    , 'Bachelor of Science Degree in Geology'
    , 'Bachelor of Science Degree in Mathematics'
    , 'Bachelor of Science in Physics with Meteorology'
    , 'Bachelor of Science in Radiation and Health Physics'
    , 'Bachelor of Science Mathematics of Finance'
    , 'Combined Bachelor of Science (Major/Major)'
    , 'Combined Bachelor of Science (Major/Minor) [Mathematics Major]'
    , 'Combined Bachelor of Science (Major/Minor) [Mathematics Minor]'
    , 'Bachelor of Arts (Political Science)'
    , 'Bachelor of Laws (LLB)'
    , 'Bachelor of Arts (Public Administration)'
    , 'Bachelor of Arts (Sociology)'
    , 'Bachelor of Arts in Criminal Justice Studies (BA CJS)'
    , 'Bachelor of Arts in Economics'
    , 'Bachelor of Arts in Population Studies'
    , 'Bachelor of Arts in Social Sciences with Psychology as Combined Major'
    , 'Bachelor of Psychology (B.Psych.)'
    , 'Bachelor of Science in Statistics'
    , 'Bachelor of Social Science Degree in Public Administration (Single Major)'
    , 'Bachelor of Social Science Degree Programme in Political Science (Single Major)'
    , 'Bachelor of Social Science Degree Programme Major in Political Science and Major in Another Subject.'
    , 'Bachelor of Social Science Degree Programme Major in Public Administration + Major in Political'
    , 'Bachelor of Social Science Degree Programme Major in Public Administration + Minor'
    , 'Bachelor of Social Science Degree Programme Major Public Administration + Other MAJOR'
    , 'Bachelor of Social Science Degree Programme: Major in Political Science and Minor in Other Subject'
    , 'Bachelor of Social Science Degree Programme: Minor in Public Administration + Major in Other Subject'
    , 'Bachelor of Social Science Degree Programme: Minor Political Science + Major in Other Subject'
    , 'Bachelor of Social Work'
    , 'Combined Bachelor of Arts (Major/Major)'
    , 'Combined Bachelor of Arts (Major/Minor) [Sociology Minor]'
    , 'Combined Bachelor of Arts in Statistics'
    , 'Combined Major Bachelor of Science in Statistics'
    , 'Diploma in Defence and Strategic Studies (DDSS)'
    , 'Diploma in Population Studies'
    , 'Diploma in Social Work (DSW)'
    , 'Diploma in Statistics', ]

properList = []

for i in listOfprograms:
    if "Bachelor of" in i:
        j = i.replace('Bachelor of ', "")
        properList.append((j,i))
    if "Combined Bachelor of" in i :
        j = i.replace('Combined Bachelor of ', "")
        properList.append((j, i))
    if "Diploma in" in i:
        j = i.replace('Diploma in ', "")
        properList.append((j, i))

print(properList)
