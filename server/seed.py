
import os
from config import db, app, bcrypt
from models import Administrator, Donor, Charity, Story
from faker import Faker
import random
from datetime import datetime

fake = Faker()
Faker.seed(42)

with app.app_context():

    print('Deleting existing data...')
    Story.query.delete()
    db.session.commit()

    Charity.query.delete()
    db.session.commit()

    Donor.query.delete()
    db.session.commit()

    Administrator.query.delete()
    db.session.commit()

     def create_admin():
        admin = Administrator()
        admin.firstname = "John"
        admin.lastname = "Doe"
        admin.email=f"{fake.unique.first_name()}.{fake.unique.last_name()}@{fake.domain_name()}",
        admin.username = "admin"
        admin._password_hash=bcrypt.generate_password_hash('password').decode('utf-8')
        db.session.add(admin)
        db.session.commit()

    def create_charities():
        charities_data = [
            {
                "title": "Kenya Red Cross Society",
                "charity_description": "The Kenya Red Cross Society (KRCS) is a non-governmental organization that works in the humanitarian field. It was founded in 1960 and is part of the International Federation of Red Cross and Red Crescent Societies. Its main goal is to help people affected by disasters or conflicts, like floods, droughts, or famines.",
                "organizer_name": "Kennedy Omunga",
                "location": "Nairobi",
                "period": str(datetime.strptime(f"{fake.date_between(start_date='-1y', end_date='today')}", '%Y-%m-%d').strftime("%d %B, %Y")) + " - " + str(datetime.strptime(f"{fake.date_between(start_date='today', end_date='+3y')}", '%Y-%m-%d').strftime("%d %B, %Y")),
                "status": "Active",
                "total_amount": 10000000,
                "administrator_id": 1,
                "donor_id": 1
            },
            {
                "title": " Heshima Kenya",
                "charity_description": "Heshima Kenya is a non-profit organization that works with children affected by HIV and AIDS. The organization provides education, food, clothing, and medical care to children who have lost their parents to AIDS.",
                "organizer_name": "Philip Karanja",
                "location": "Nairobi",
                "period": str(datetime.strptime(f"{fake.date_between(start_date='-1y', end_date='today')}", '%Y-%m-%d').strftime("%d %B, %Y")) + " - " + str(datetime.strptime(f"{fake.date_between(start_date='today', end_date='+3y')}", '%Y-%m-%d').strftime("%d %B, %Y")),
                "status": "Inactive",
                "total_amount": 400000,
                "administrator_id": 1,
                "donor_id": 2
            },
            {
                "title": " Food for Education Organization-Kenya(FEOK)",
                "charity_description": "FEOK is a non-governmental organization that aims to provide food and education to children in Kenya. The main objective is to provide meals for children from low-income families so they can attend school regularly. It also aims to improve nutritional status, physical growth, and cognitive development.",
                "organizer_name": "Caren Chebet",
                "location": "Kisumu",
                "period": str(datetime.strptime(f"{fake.date_between(start_date='-1y', end_date='today')}", '%Y-%m-%d').strftime("%d %B, %Y")) + " - " + str(datetime.strptime(f"{fake.date_between(start_date='today', end_date='+3y')}", '%Y-%m-%d').strftime("%d %B, %Y")),
                "status": "Active",
                "total_amount": 5000,
                "administrator_id": 1,
                "donor_id": 3
            },
            {
                "title": "Nakuru Children’s Rescue and Rehabilitation Centre (NACCER)",
                "charity_description": "Nakuru Children’s Rescue and Rehabilitation Centre (NACCER) is a non-profit organization that works to protect children from abuse, neglect, and exploitation. NACCER provides a safe home for children who have been abused, abandoned, or neglected. They also work with the community to prevent abuse and neglect by offering health education programs, workshops on parenting skills, and counseling services.",
                "organizer_name": "Karanja Wamwega",
                "location": "Nakuru",
                "period": str(datetime.strptime(f"{fake.date_between(start_date='-1y', end_date='today')}", '%Y-%m-%d').strftime("%d %B, %Y")) + " - " + str(datetime.strptime(f"{fake.date_between(start_date='today', end_date='+3y')}", '%Y-%m-%d').strftime("%d %B, %Y")),
                "status": "Active",
                "total_amount": 60000,
                "administrator_id": 1,
                "donor_id": 4
            },
            {
                "title": "Ebenezer Foundation",
                "charity_description": "Ebenezer Christian Children’s Home was founded in 1994 as an avenue to provide a loving, Christian environment to children removed from their homes due to neglect or abuse. ECCH is a fully licensed North Carolina Residential Child-Care Facility, and a 501 (c)(3) nonprofit organization. Ebenezer Christian Children’s Home believes that God has called us to continually share Christ’s love with all those who pass our way. We seek to minister to the spiritual, physical, emotional, and educational needs of the children that have been placed in our care. ",
                "organizer_name": "Barry Byrd",
                "location": "North California",
                "period": str(datetime.strptime(f"{fake.date_between(start_date='-1y', end_date='today')}", '%Y-%m-%d').strftime("%d %B, %Y")) + " - " + str(datetime.strptime(f"{fake.date_between(start_date='today', end_date='+3y')}", '%Y-%m-%d').strftime("%d %B, %Y")),
                "status": "Active",
                "total_amount": 50000,
                "administrator_id": 1,
                "donor_id": 5
            },
            {
                "title": " The Royal Seed Orphanage",
                "charity_description": "The Royal Seed Orphanage has a team of dedicated volunteers who assist with day-to-day operations. They ensure that all children are cared for and given access to nutritious food and clean water. The orphanage also provides education and sports facilities for the children to grow up healthy and happy.",
                "organizer_name": "Purity Mukuba",
                "location": "Meru",
                "period": str(datetime.strptime(f"{fake.date_between(start_date='-1y', end_date='today')}", '%Y-%m-%d').strftime("%d %B, %Y")) + " - " + str(datetime.strptime(f"{fake.date_between(start_date='today', end_date='+3y')}", '%Y-%m-%d').strftime("%d %B, %Y")),
                "status": "Active",
                "total_amount": 30000,
                "administrator_id": 1,
                "donor_id": 6
            },
            {
                "title": "The Education for All Scholarship ",
                "charity_description": "The Education for All Scholarship is a transformative initiative dedicated to providing financial support and educational opportunities to deserving students worldwide. By removing financial barriers, the scholarship empowers individuals to pursue their academic goals and unlock their full potential. Through its commitment to educational equity and inclusivity, the program strives to create a brighter future for all.",
                "organizer_name": " Dennis Ochieng",
                "location": "Kakamega",
                "period": str(datetime.strptime(f"{fake.date_between(start_date='-1y', end_date='today')}", '%Y-%m-%d').strftime("%d %B, %Y")) + " - " + str(datetime.strptime(f"{fake.date_between(start_date='today', end_date='+3y')}", '%Y-%m-%d').strftime("%d %B, %Y")),
                "status": "Closed",
                "total_amount": 300000,
                "administrator_id": 1,
                "donor_id": 7
            }, 
            {
                "title": " Habitat for Humanity",
                "charity_description": "Habitat for Humanity works to build affordable housing and provide shelter to families in need around the world.",
                "organizer_name": "Jeff Clinton",
                "location": "Nairobi",
                "period": str(datetime.strptime(f"{fake.date_between(start_date='-1y', end_date='today')}", '%Y-%m-%d').strftime("%d %B, %Y")) + " - " + str(datetime.strptime(f"{fake.date_between(start_date='today', end_date='+3y')}", '%Y-%m-%d').strftime("%d %B, %Y")),
                "status": "Active",
                "total_amount": 1200000,
                "administrator_id": 1,
                "donor_id": 8
            },  
            {
                "title": "World Wildlife Fund (WWF)",
                "charity_description": "WWF is dedicated to conservation efforts to protect endangered species and their habitats, as well as promoting sustainable practices to address environmental challenges.",
                "organizer_name": "Organizer 2",
                "location": "Nairobi",
                "period": str(datetime.strptime(f"{fake.date_between(start_date='-1y', end_date='today')}", '%Y-%m-%d').strftime("%d %B, %Y")) + " - " + str(datetime.strptime(f"{fake.date_between(start_date='today', end_date='+3y')}", '%Y-%m-%d').strftime("%d %B, %Y")),
                "status": "Active",
                "total_amount": 25000,
                "administrator_id": 1,
                "donor_id": 8
            }, 
            {
                "title": "Kiambu County Women's Association (KIACOWA)",
                "charity_description": "KIACOWA is a local non-profit organization based in Kiambu County, Kenya, dedicated to empowering women and promoting community development. Founded by a group of passionate women leaders, KIACOWA focuses on various initiatives aimed at improving the lives of women, children, and families in the region. These initiatives may include skills training programs, economic empowerment projects, healthcare services, education support, and advocacy for women's rights and gender equality. Through its grassroots approach and community engagement, KIACOWA strives to address the unique challenges faced by women and vulnerable populations in Kiambu County, fostering sustainable development and positive social change.",
                "organizer_name": "Adena Kane",
                "location": "Kiambu",
                "period": str(datetime.strptime(f"{fake.date_between(start_date='-1y', end_date='today')}", '%Y-%m-%d').strftime("%d %B, %Y")) + " - " + str(datetime.strptime(f"{fake.date_between(start_date='today', end_date='+3y')}", '%Y-%m-%d').strftime("%d %B, %Y")),
                "status": "Active",
                "total_amount": 100000,
                "administrator_id": 1,
                "donor_id": 1
            },
            {
                "title": "Moi Teaching and Referral Hospital (MTRH) Friends of Cancer Patients Support Group:",
                "charity_description": "The MTRH Friends of Cancer Patients Support Group is a community-based organization in Eldoret dedicated to providing support and assistance to cancer patients and their families. Through emotional support, counseling, financial aid, and advocacy efforts, the group aims to alleviate the burdens faced by cancer patients and improve their quality of life. By fostering community solidarity and raising awareness about cancer prevention and treatment, the group plays a vital role in empowering patients and promoting early detection.",
                "organizer_name": "Jediel Kiptum",
                "location": "Eldoret",
                "period": str(datetime.strptime(f"{fake.date_between(start_date='-1y', end_date='today')}", '%Y-%m-%d').strftime("%d %B, %Y")) + " - " + str(datetime.strptime(f"{fake.date_between(start_date='today', end_date='+3y')}", '%Y-%m-%d').strftime("%d %B, %Y")),
                "status": "Active",
                "total_amount": 30000,
                "administrator_id": 1,
                "donor_id": 1
            },
            {
                "title": "Sanergy"
                "charity_description": "Sanergy builds and franchises low-cost sanitation facilities while converting waste into renewable energy and organic fertilizer."
                "organizer_name": "Barasa Omondi",
                "location" : "Kisumu",
                "period": str(datetime.strptime(f"{fake.date_between(start_date='-1y', end_date='today')}", '%Y-%m-%d').strftime("%d %B, %Y")) + " - " + str(datetime.strptime(f"{fake.date_between(start_date='today', end_date='+3y')}", '%Y-%m-%d').strftime("%d %B, %Y")),
                "status": "Active",
                "total_amount": 250000,
                "administrator_id": 1,
                "donor_id": 9
            },
            {
                "title": "Concern Worldwide Kenya",
                "charity_description": "Concern Worldwide Kenya implements integrated water, sanitation, and hygiene (WASH) programs, aiming to alleviate poverty and improve health outcomes in vulnerable communities across Kenya."
                "organizer_name": "Kamau Njuguna",
                "location" : "Kericho",
                "period": str(datetime.strptime(f"{fake.date_between(start_date='-1y', end_date='today')}", '%Y-%m-%d').strftime("%d %B, %Y")) + " - " + str(datetime.strptime(f"{fake.date_between(start_date='today', end_date='+3y')}", '%Y-%m-%d').strftime("%d %B, %Y")),
                "status": "Active",
                "total_amount": 100000,
                "administrator_id": 1,
                "donor_id": 10
            },
            {
                "title": "Africa Sand Dam Foundation"
                "charity_description": "Africa Sand Dam Foundation constructs sand dams and promotes water harvesting techniques to improve water availability and sanitation in arid and semi-arid regions of Kenya."
                "organizer_name": "Wafula Wambua",
                "location" : "Nandi",
                "period": str(datetime.strptime(f"{fake.date_between(start_date='-1y', end_date='today')}", '%Y-%m-%d').strftime("%d %B, %Y")) + " - " + str(datetime.strptime(f"{fake.date_between(start_date='today', end_date='+3y')}", '%Y-%m-%d').strftime("%d %B, %Y")),
                "status": "Active",
                "total_amount": 15000,
                "administrator_id": 1,
                "donor_id": 7

            },
            {
                "title": "Oxfam in Kenya"
                "charity_description": "Oxfam in Kenya provides humanitarian assistance and supports community-based sanitation projects, focusing on vulnerable populations and marginalized communities."
                "organizer_name": "Mugo Githinji",
                "location" : "Isiolo",
                "period": str(datetime.strptime(f"{fake.date_between(start_date='-1y', end_date='today')}", '%Y-%m-%d').strftime("%d %B, %Y")) + " - " + str(datetime.strptime(f"{fake.date_between(start_date='today', end_date='+3y')}", '%Y-%m-%d').strftime("%d %B, %Y")),
                "status": "Active",
                "total_amount": 90000,
                "administrator_id": 1,
                "donor_id": 5
            },
            {
                "title": "Western Kenya Community Driven Development and Flood Mitigation Project"
                "charity_description": "Western Kenya Community Driven Development and Flood Mitigation Project empowers communities to manage water resources and mitigate flood-related sanitation risks in western Kenya."
                "organizer_name": "Kariuki Waweru",
                "location" : "Turkana",
                "period": str(datetime.strptime(f"{fake.date_between(start_date='-1y', end_date='today')}", '%Y-%m-%d').strftime("%d %B, %Y")) + " - " + str(datetime.strptime(f"{fake.date_between(start_date='today', end_date='+3y')}", '%Y-%m-%d').strftime("%d %B, %Y")),
                "status": "Active",
                "total_amount": 60000,
                "administrator_id": 1,
                "donor_id": 12
            },
            {
                "title": "Center for Health Solutions Kenya (CHS)"
                "charity_description": "Center for Health Solutions Kenya (CHS) implements sanitation and hygiene programs in healthcare facilities, promoting infection prevention and control to improve health outcomes."
                "organizer_name": "Muthoni Nyaga",
                "location" : "Kapsabet",
                "period": str(datetime.strptime(f"{fake.date_between(start_date='-1y', end_date='today')}", '%Y-%m-%d').strftime("%d %B, %Y")) + " - " + str(datetime.strptime(f"{fake.date_between(start_date='today', end_date='+3y')}", '%Y-%m-%d').strftime("%d %B, %Y")),
                "status": "Active",
                "total_amount": 160000,
                "administrator_id": 1,
                "donor_id": 14
            },
            {
                "title": "ChildFund Kenya"
                "charity_description": "ChildFund Kenya integrates sanitation initiatives into child-focused development programs, aiming to improve health and well-being among children and their families."
                "organizer_name": "Chemutai Kibet",
                "location" : "Kitale",
                "period": str(datetime.strptime(f"{fake.date_between(start_date='-1y', end_date='today')}", '%Y-%m-%d').strftime("%d %B, %Y")) + " - " + str(datetime.strptime(f"{fake.date_between(start_date='today', end_date='+3y')}", '%Y-%m-%d').strftime("%d %B, %Y")),
                "status": "Active",
                "total_amount": 230000,
                "administrator_id": 1,
                "donor_id": 4 
            },
            {
                "title": "Maji Milele"
                "charity_description": "Maji Milele operates water kiosks and community sanitation facilities, ensuring affordable and sustainable water and sanitation services for communities."
                "organizer_name": "Otieno Owiti",
                "location" : "Machakos",
                "period": str(datetime.strptime(f"{fake.date_between(start_date='-1y', end_date='today')}", '%Y-%m-%d').strftime("%d %B, %Y")) + " - " + str(datetime.strptime(f"{fake.date_between(start_date='today', end_date='+3y')}", '%Y-%m-%d').strftime("%d %B, %Y")),
                "status": "Active",
                "total_amount": 50000,
                "administrator_id": 1,
                "donor_id": 15 
            },
            {
                "title": "Rural Water and Sanitation Support Programme (RWASSP)"
                "charity_description": "Rural Water and Sanitation Support Programme (RWASSP) provides technical and financial support for rural water supply and sanitation projects, enhancing access to clean water and sanitation facilities."
                "organizer_name": "Makena Wanjiru",
                "location" : "Nyeri",
                "period": str(datetime.strptime(f"{fake.date_between(start_date='-1y', end_date='today')}", '%Y-%m-%d').strftime("%d %B, %Y")) + " - " + str(datetime.strptime(f"{fake.date_between(start_date='today', end_date='+3y')}", '%Y-%m-%d').strftime("%d %B, %Y")),
                "status": "Active",
                "total_amount": 700000,
                "administrator_id": 1,
                "donor_id": 20
            },
            {
                "title": "Sustainable Aid in Africa International (SANA) Kenya"
                "charity_description": "Sustainable Aid in Africa International (SANA) Kenya Implements sanitation projects in rural communities, focusing on community participation and capacity building."
                "organizer_name": "Anyango Odhiambo"
                "location" : "Nyahururu",
                "period": str(datetime.strptime(f"{fake.date_between(start_date='-1y', end_date='today')}", '%Y-%m-%d').strftime("%d %B, %Y")) + " - " + str(datetime.strptime(f"{fake.date_between(start_date='today', end_date='+3y')}", '%Y-%m-%d').strftime("%d %B, %Y")),
                "status": "Active",
                "total_amount": 220000,
                "administrator_id": 1,
                "donor_id": 19
            },
            {

                "title": "Nairobi City Water and Sewerage Company"
                "charity_description": "Nairobi City Water and Sewerage Company manages water and sewerage services in Nairobi, ensuring access to clean water and proper sanitation facilities for residents."
                "organizer_name": "Kiptoo Kiprop",
                "location" : "Nyahururu",
                "period": str(datetime.strptime(f"{fake.date_between(start_date='-1y', end_date='today')}", '%Y-%m-%d').strftime("%d %B, %Y")) + " - " + str(datetime.strptime(f"{fake.date_between(start_date='today', end_date='+3y')}", '%Y-%m-%d').strftime("%d %B, %Y")),
                "status": "Active",
                "total_amount": 31000,
                "administrator_id": 1,
                "donor_id": 17
            },
            {
                "title": "Amref Health Africa"
                "charity_description": "Amref Health Africa implements community-led sanitation projects, emphasizing behavior change, hygiene promotion, and infrastructure development."
                "organizer_name": "Nyaga Mwangi",
                "location" : "Uasin Gishu",
                "period": str(datetime.strptime(f"{fake.date_between(start_date='-1y', end_date='today')}", '%Y-%m-%d').strftime("%d %B, %Y")) + " - " + str(datetime.strptime(f"{fake.date_between(start_date='today', end_date='+3y')}", '%Y-%m-%d').strftime("%d %B, %Y")),
                "status": "Active",
                "total_amount": 45000,
                "administrator_id": 1,
                "donor_id": 18
            },
            {
                "title": "Water & Sanitation for the Urban Poor (WSUP) Kenya"
                "charity_description": "Water & Sanitation for the Urban Poor (WSUP) Kenya implements water and sanitation projects in urban slums, aiming to improve living conditions and health outcomes."
                "organizer_name": "Njeri Kamau",
                "location" : "Juja",
                "period": str(datetime.strptime(f"{fake.date_between(start_date='-1y', end_date='today')}", '%Y-%m-%d').strftime("%d %B, %Y")) + " - " + str(datetime.strptime(f"{fake.date_between(start_date='today', end_date='+3y')}", '%Y-%m-%d').strftime("%d %B, %Y")),
                "status": "Active",
                "total_amount": 500000,
                "administrator_id": 1,
                "donor_id": 20
            },
            {
                "title": "Sanitation and Water for All Kenya"
                "charity_description": "Sanitation and Water for All Kenya advocates for improved sanitation policies and works towards achieving universal access to water and sanitation in Kenya."
                "organizer_name": "Chege Maina",
                "location" : "Nakuru",
                "period": str(datetime.strptime(f"{fake.date_between(start_date='-1y', end_date='today')}", '%Y-%m-%d').strftime("%d %B, %Y")) + " - " + str(datetime.strptime(f"{fake.date_between(start_date='today', end_date='+3y')}", '%Y-%m-%d').strftime("%d %B, %Y")),
                "status": "Active",
                "total_amount": 100000,
                "administrator_id": 1,
                "donor_id": 7 
            },
            {
                "title": "Sanergy"
                "charity_description": "Sanergy builds and franchises low-cost sanitation facilities while converting waste into renewable energy and organic fertilizer."
                "organizer_name": "Barasa Omondi",
                "location" : "Vihiga",
                "period": str(datetime.strptime(f"{fake.date_between(start_date='-1y', end_date='today')}", '%Y-%m-%d').strftime("%d %B, %Y")) + " - " + str(datetime.strptime(f"{fake.date_between(start_date='today', end_date='+3y')}", '%Y-%m-%d').strftime("%d %B, %Y")),
                "status": "Active",
                "total_amount": 3000000,
                "administrator_id": 1,
                "donor_id": 6 
            },
            {
                "title": "Clean Water Kenya",
                "charity_description": "Clean Water Kenya focuses on providing clean and safe drinking water to rural communities in Kenya.",
                "organizer_name": "Jane Wanjiku",
                "location": "Nairobi",
                "period": "Start Date - End Date",
                "status": "Active",
                "total_amount": 75000,
                "administrator_id": 1,
                "donor_id": 3
            },
            {
                "title": "Kenya Wildlife Trust",
                "charity_description": "Kenya Wildlife Trust is dedicated to conserving Kenya's wildlife and habitats through community engagement and education programs.",
                "organizer_name": "David Mwangi",
                "location": "Masai Mara",
                "period": "Start Date - End Date",
                "status": "Active",
                "total_amount": 200000,
                "administrator_id": 1,
                "donor_id": 7
            },
            {
                "title": "Kenya Health Initiative",
                "charity_description": "Kenya Health Initiative works to improve healthcare access and outcomes for underserved populations in Kenya.",
                "organizer_name": "Grace Akinyi",
                "location": "Kisumu",
                "period": "Start Date - End Date",
                "status": "Active",
                "total_amount": 50000,
                "administrator_id": 1,
                "donor_id": 8
            },
            {
                "title": "Kenya Education Foundation",
                "charity_description": "Kenya Education Foundation provides scholarships and educational resources to disadvantaged students across Kenya.",
                "organizer_name": "Samuel Ndungu",
                "location": "Nakuru",
                "period": str(datetime.strptime(f"{fake.date_between(start_date='-1y', end_date='today')}", '%Y-%m-%d').strftime("%d %B, %Y")) + " - " + str(datetime.strptime(f"{fake.date_between(start_date='today', end_date='+3y')}", '%Y-%m-%d').strftime("%d %B, %Y")),
                "status": "Active",
                "total_amount": 100000,
                "administrator_id": 1,
                "donor_id": 9
            },
            {
                "title": "Kenya Food Bank",
                "charity_description": "Kenya Food Bank collects and distributes food to alleviate hunger and malnutrition in impoverished communities throughout Kenya.",
                "organizer_name": "Alice Wambui",
                "location": "Mombasa",
                "period": str(datetime.strptime(f"{fake.date_between(start_date='-1y', end_date='today')}", '%Y-%m-%d').strftime("%d %B, %Y")) + " - " + str(datetime.strptime(f"{fake.date_between(start_date='today', end_date='+3y')}", '%Y-%m-%d').strftime("%d %B, %Y")),
                "status": "Active",
                "total_amount": 60000,
                "administrator_id": 1,
                "donor_id": 10
            },
            {
                "title": "Kenya Community Development Foundation",
                "charity_description": "Kenya Community Development Foundation works to empower local communities through sustainable development projects, focusing on education, healthcare, and economic empowerment.",
                "organizer_name": "Josephine Achieng",
                "location": "Kisii",
                "period": str(datetime.strptime(f"{fake.date_between(start_date='-1y', end_date='today')}", '%Y-%m-%d').strftime("%d %B, %Y")) + " - " + str(datetime.strptime(f"{fake.date_between(start_date='today', end_date='+3y')}", '%Y-%m-%d').strftime("%d %B, %Y")),
                "status": "Active",
                "total_amount": 80000,
                "administrator_id": 1,
                "donor_id": 11
            },
            {
                "title": "Kenya Conservation Society",
                "charity_description": "Kenya Conservation Society is dedicated to preserving Kenya's natural heritage by promoting conservation efforts and environmental education.",
                "organizer_name": "Peter Kimani",
                "location": "Nanyuki",
                "period": str(datetime.strptime(f"{fake.date_between(start_date='-1y', end_date='today')}", '%Y-%m-%d').strftime("%d %B, %Y")) + " - " + str(datetime.strptime(f"{fake.date_between(start_date='today', end_date='+3y')}", '%Y-%m-%d').strftime("%d %B, %Y")),
                "status": "Active",
                "total_amount": 120000,
                "administrator_id": 1,
                "donor_id": 12
            },
            {
                "title": "Kenya Youth Empowerment Network",
                "charity_description": "Kenya Youth Empowerment Network provides vocational training, mentorship, and entrepreneurial support to young people in Kenya, empowering them to become self-reliant and productive members of society.",
                "organizer_name": "Lucy Njeri",
                "location": "Thika",
                "period": str(datetime.strptime(f"{fake.date_between(start_date='-1y', end_date='today')}", '%Y-%m-%d').strftime("%d %B, %Y")) + " - " + str(datetime.strptime(f"{fake.date_between(start_date='today', end_date='+3y')}", '%Y-%m-%d').strftime("%d %B, %Y")),
                "status": "Active",
                "total_amount": 70000,
                "administrator_id": 1,
                "donor_id": 13
            },
            {
                "title": "Kenya Women's Health Initiative",
                "charity_description": "Kenya Women's Health Initiative focuses on improving women's health outcomes through education, access to healthcare services, and advocacy for women's rights.",
                "organizer_name": "Esther Nyambura",
                "location": "Eldoret",
                "period": str(datetime.strptime(f"{fake.date_between(start_date='-1y', end_date='today')}", '%Y-%m-%d').strftime("%d %B, %Y")) + " - " + str(datetime.strptime(f"{fake.date_between(start_date='today', end_date='+3y')}", '%Y-%m-%d').strftime("%d %B, %Y")),
                "status": "Active",
                "total_amount": 90000,
                "administrator_id": 1,
                "donor_id": 14
            },
            {
                "title": "Kenya Environmental Conservation Alliance",
                "charity_description": "Kenya Environmental Conservation Alliance works with local communities to promote sustainable land use practices, biodiversity conservation, and climate change adaptation in Kenya.",
                "organizer_name": "James Mugo",
                "location": "Naivasha",
                "period": str(datetime.strptime(f"{fake.date_between(start_date='-1y', end_date='today')}", '%Y-%m-%d').strftime("%d %B, %Y")) + " - " + str(datetime.strptime(f"{fake.date_between(start_date='today', end_date='+3y')}", '%Y-%m-%d').strftime("%d %B, %Y")),
                "status": "Active",
                "total_amount": 100000,
                "administrator_id": 1,
                "donor_id": 15
            },
            {
                "title": "Kenya Rural Development Initiative",
                "charity_description": "Kenya Rural Development Initiative focuses on sustainable development projects tailored to the needs of rural communities, including agriculture, infrastructure, and education.",
                "organizer_name": "Pauline Chepkorir",
                "location": "Kericho",
                "period": str(datetime.strptime(f"{fake.date_between(start_date='-1y', end_date='today')}", '%Y-%m-%d').strftime("%d %B, %Y")) + " - " + str(datetime.strptime(f"{fake.date_between(start_date='today', end_date='+3y')}", '%Y-%m-%d').strftime("%d %B, %Y")),
                "status": "Active",
                "total_amount": 85000,
                "administrator_id": 1,
                "donor_id": 16
            },
            {
                "title": "Kenya Hope Foundation",
                "charity_description": "Kenya Hope Foundation provides comprehensive support to orphaned and vulnerable children in Kenya, including shelter, education, healthcare, and psychosocial services.",
                "organizer_name": "Daniel Ochieng",
                "location": "Kisumu",
                "period": str(datetime.strptime(f"{fake.date_between(start_date='-1y', end_date='today')}", '%Y-%m-%d').strftime("%d %B, %Y")) + " - " + str(datetime.strptime(f"{fake.date_between(start_date='today', end_date='+3y')}", '%Y-%m-%d').strftime("%d %B, %Y")),
                "status": "Active",
                "total_amount": 95000,
                "administrator_id": 1,
                "donor_id": 17
            },
            {
                "title": "Kenya Sustainable Agriculture Initiative",
                "charity_description": "Kenya Sustainable Agriculture Initiative promotes environmentally friendly farming practices, soil conservation, and sustainable livelihoods among smallholder farmers in Kenya.",
                "organizer_name": "Beatrice Wambui",
                "location": "Nakuru",
                "period": str(datetime.strptime(f"{fake.date_between(start_date='-1y', end_date='today')}", '%Y-%m-%d').strftime("%d %B, %Y")) + " - " + str(datetime.strptime(f"{fake.date_between(start_date='today', end_date='+3y')}", '%Y-%m-%d').strftime("%d %B, %Y")),
                "status": "Active",
                "total_amount": 80000,
                "administrator_id": 1,
                "donor_id": 18
            },
            {
                "title": "Kenya Education Access Project",
                "charity_description": "Kenya Education Access Project works to improve access to quality education for marginalized and disadvantaged children in Kenya through scholarships, school infrastructure development, and teacher training programs.",
                "organizer_name": "Patrick Maina",
                "location": "Machakos",
                "period": str(datetime.strptime(f"{fake.date_between(start_date='-1y', end_date='today')}", '%Y-%m-%d').strftime("%d %B, %Y")) + " - " + str(datetime.strptime(f"{fake.date_between(start_date='today', end_date='+3y')}", '%Y-%m-%d').strftime("%d %B, %Y")),
                "status": "Active",
                "total_amount": 110000,
                "administrator_id": 1,
                "donor_id": 19
            },
            {
                "title": "Kenya Community Health Initiative",
                "charity_description": "Kenya Community Health Initiative focuses on improving community health outcomes through preventive healthcare programs, health education, and access to essential medical services.",
                "organizer_name": "Mercy Auma",
                "location": "Homabay",
                "period": str(datetime.strptime(f"{fake.date_between(start_date='-1y', end_date='today')}", '%Y-%m-%d').strftime("%d %B, %Y")) + " - " + str(datetime.strptime(f"{fake.date_between(start_date='today', end_date='+3y')}", '%Y-%m-%d').strftime("%d %B, %Y")),
                "status": "Active",
                "total_amount": 75000,
                "administrator_id": 1,
                "donor_id": 20
            },
            {
                "title": "Kenya Wildlife Conservation Society",
                "charity_description": "The Kenya Wildlife Conservation Society is dedicated to the protection and conservation of Kenya's rich biodiversity, including wildlife species and their habitats. Through research, community engagement, and advocacy, the organization works to mitigate threats to wildlife and promote sustainable conservation practices.",
                "organizer_name": "Josephat Mwangi",
                "location": "Nairobi",
                "period": str(datetime.strptime(f"{fake.date_between(start_date='-1y', end_date='today')}", '%Y-%m-%d').strftime("%d %B, %Y")) + " - " + str(datetime.strptime(f"{fake.date_between(start_date='today', end_date='+3y')}", '%Y-%m-%d').strftime("%d %B, %Y")),
                "status": "Active",
                "total_amount": 120000,
                "administrator_id": 1,
                "donor_id": 21
            },
            {
                "title": "Kenya Clean Energy Initiative",
                "charity_description": "The Kenya Clean Energy Initiative focuses on promoting access to clean and renewable energy solutions across Kenya. Through projects such as solar electrification, biogas systems, and energy-efficient technologies, the organization aims to improve energy access, reduce environmental impact, and enhance livelihoods in rural and underserved communities.",
                "organizer_name": "Grace Wanjiku",
                "location": "Mombasa",
                "period": str(datetime.strptime(f"{fake.date_between(start_date='-1y', end_date='today')}", '%Y-%m-%d').strftime("%d %B, %Y")) + " - " + str(datetime.strptime(f"{fake.date_between(start_date='today', end_date='+3y')}", '%Y-%m-%d').strftime("%d %B, %Y")),
                "status": "Active",
                "total_amount": 95000,
                "administrator_id": 1,
                "donor_id": 22
                        },
            {
                "title": "Kenya Mental Health Support Foundation",
                "charity_description": "The Kenya Mental Health Support Foundation provides advocacy, awareness, and support services for individuals affected by mental health issues in Kenya. Through community outreach, counseling, and education programs, the organization works to reduce stigma, increase access to mental healthcare, and promote mental well-being.",
                "organizer_name": "Lucas Muthoni",
                "location": "Nairobi",
                "period": str(datetime.strptime(f"{fake.date_between(start_date='-1y', end_date='today')}", '%Y-%m-%d').strftime("%d %B, %Y")) + " - " + str(datetime.strptime(f"{fake.date_between(start_date='today', end_date='+3y')}", '%Y-%m-%d').strftime("%d %B, %Y")),
                "status": "Active",
                "total_amount": 85000,
                "administrator_id": 1,
                "donor_id": 23
            },
            {
                "title": "Kenya Sustainable Tourism Alliance",
                "charity_description": "The Kenya Sustainable Tourism Alliance promotes sustainable tourism practices that benefit local communities, conserve natural resources, and preserve cultural heritage. By working with tourism stakeholders, the organization aims to create positive socio-economic impacts, protect biodiversity, and enhance the long-term viability of Kenya's tourism industry.",
                "organizer_name": "Sarah Kipchoge",
                "location": "Nairobi",
                "period": str(datetime.strptime(f"{fake.date_between(start_date='-1y', end_date='today')}", '%Y-%m-%d').strftime("%d %B, %Y")) + " - " + str(datetime.strptime(f"{fake.date_between(start_date='today', end_date='+3y')}", '%Y-%m-%d').strftime("%d %B, %Y")),
                "status": "Active",
                "total_amount": 110000,
                "administrator_id": 1,
                "donor_id": 24
            },
            {
                "title": "Kenya Food Security Initiative",
                "charity_description": "The Kenya Food Security Initiative addresses food insecurity and malnutrition by implementing sustainable agriculture projects, promoting access to nutritious food, and empowering local farmers. Through initiatives such as crop diversification, irrigation systems, and farmer training programs, the organization works to improve food production, income generation, and food access for vulnerable communities.",
                "organizer_name": "John Njoroge",
                "location": "Eldoret",
                "period": str(datetime.strptime(f"{fake.date_between(start_date='-1y', end_date='today')}", '%Y-%m-%d').strftime("%d %B, %Y")) + " - " + str(datetime.strptime(f"{fake.date_between(start_date='today', end_date='+3y')}", '%Y-%m-%d').strftime("%d %B, %Y")),
                "status": "Active",
                "total_amount": 100000,
                "administrator_id": 1,
                "donor_id": 25
            }
        ]
        for charity_data in charities_data:
            charity = Charity(**charity_data)
            db.session.add(charity)
        db.session.commit()


    def create_donor_seed():
        donors_data =[
            {"firstname": "Chris ", "lastname": "Bolick", "username": "chrisBolick", "password": "password123", "amount": 20000},
            {"firstname": "Joey", "lastname": "Stony", "username": "Joeystony", "password": "password456", "amount": 100000},
            {"firstname": "Faith", "lastname": "Atieno", "username": "faithatieno", "password": "password234", "amount": 200000},
            {"firstname": "Kiraitu", "lastname": "Murungi", "username": "kiraitu", "password": "password456", "amount": 50000},
            {"firstname": "Emily", "lastname": "Wangari", "username": "emilyw", "password": "password456", "amount": 2500000},
            {"firstname": "Raymond", "lastname": "Omondi", "username": "rayo", "password": "password123", "amount": 300000},
            {"firstname": "Phyilis", "lastname": "Makena", "username": "makenap", "password": "password236", "amount": 5000000},
            {"firstname": "Todd ", "lastname": "Josh", "username": "toddjosh", "password": "pass12334", "amount": 50000},
            {"firstname": "Alice", "lastname": "Johnson", "username": "alicejohnson", "password": "password789", "amount": 150000},
            {"firstname": "Michael", "lastname": "Smith", "username": "michaelsmith", "password": "password321", "amount": 75000},
            {"firstname": "Sarah", "lastname": "Connor", "username": "sarahconnor", "password": "password654", "amount": 500000},
            {"firstname": "David", "lastname": "Brown", "username": "davidbrown", "password": "password987", "amount": 120000},
            {"firstname": "Linda", "lastname": "White", "username": "lindawhite", "password": "password321", "amount": 95000},
            {"firstname": "James", "lastname": "Wilson", "username": "jameswilson", "password": "password852", "amount": 67000},
            {"firstname": "Sophia", "lastname": "Martinez", "username": "sophiamartinez", "password": "password963", "amount": 200000},
            {"firstname": "Ethan", "lastname": "Lee", "username": "ethanlee", "password": "password741", "amount": 130000},
            {"firstname": "Isabella", "lastname": "Garcia", "username": "isabellagarcia", "password": "password852", "amount": 250000},
            {"firstname": "Jacob", "lastname": "Miller", "username": "jacobmiller", "password": "password159", "amount": 180000},
            {"firstname": "Emma", "lastname": "Davis", "username": "emmadavis", "password": "password753", "amount": 110000},
            {"firstname": "Daniel", "lastname": "kamau", "username": "daniellopez", "password": "password159", "amount": 60000},
            {"firstname": "Sophie", "lastname": "Smith", "username": "sophiesmith", "password": "password852", "amount": 300000},
            {"firstname": "Oliver", "lastname": "Johnson", "username": "oliverjohnson", "password": "password159", "amount": 240000},
            {"firstname": "Ava", "lastname": "Brown", "username": "avabrown", "password": "password753", "amount": 70000},
            {"firstname": "Matthew", "lastname": "Clark", "username": "matthewclark", "password": "password456", "amount": 280000},
            {"firstname": "Chloe", "lastname": "Anderson", "username": "chloeanderson", "password": "password789", "amount": 90000},
            {"firstname": "Benjamin", "lastname": "Thompson", "username": "benthompson", "password": "password123", "amount": 160000},
            {"firstname": "Mia", "lastname": "Thomas", "username": "miathomas", "password": "password456", "amount": 220000},
            {"firstname": "William", "lastname": "Harris", "username": "williamharris", "password": "password987", "amount": 75000},
            {"firstname": "Natalie", "lastname": "Young", "username": "natalieyoung", "password": "password321", "amount": 110000},
            {"firstname": "Andrew", "lastname": "King", "username": "andrewking", "password": "password852", "amount": 85000},
            {"firstname": "Victoria", "lastname": "Evans", "username": "victoriaevans", "password": "password963", "amount": 300000},
            {"firstname": "Gabriel", "lastname": "Thomas", "username": "gabrielthomas", "password": "password741", "amount": 130000},
            {"firstname": "Madison", "lastname": "Russell", "username": "madisonrussell", "password": "password852", "amount": 200000}
        ]

        for donor_info in donors_data:
            donor = Donor(
                firstname=donor_info["firstname"],
                lastname=donor_info["lastname"],
                username=donor_info["username"],
                password_hash=donor_info["password"],  
                amount=donor_info["amount"]
            )
            db.session.add(donor)
        db.session.commit()

    def seed_stories():
        stories_data = [
            {
                "beneficiary_name": "mutunga school",
                "beneficiary_story": "The Education for All Scholarship Fund extends heartfelt gratitude to our donors whose contributions have transformed lives. Through your generosity, we've been able to award scholarships to deserving students, empowering them to pursue their dreams of higher education. Your support has opened doors of opportunity for talented individuals from diverse backgrounds, allowing them to excel academically and contribute positively to society. Together, we're making education accessible and creating a brighter future for our communities.",
                "charity_id": 7
            },
            {
                "beneficiary_name": "Communities Affected by Disasters",
                "beneficiary_story":"Thanks to the unwavering support of the Kenya Red Cross Society, countless lives have been saved and communities uplifted in times of crisis. Whether responding to natural disasters like floods, droughts, or famines, or providing vital medical assistance during emergencies, the Kenya Red Cross Society remains a beacon of hope for those in need. With its dedicated volunteers and tireless efforts, the organization continues to make a profound impact, offering comfort, aid, and a sense of security to vulnerable populations across Kenya.",
                "charity_id": 1
            },
            {
                "beneficiary_name": "Local School Donation",
                "beneficiary_story": "Our local school received a generous donation from the community. Thanks to everyone's support, we were able to purchase new books, educational materials, and sports equipment. The students are thrilled and grateful for the opportunity to learn and play in an enriched environment.",
                "charity_id": 5
            },
            {
                "beneficiary_name":"Vulnerable Children in Nakuru",
                "Beneficiary Story" : "NACCER's unwavering commitment to protecting and nurturing vulnerable children has made a lasting impact on the community of Nakuru. By providing a safe haven for children who have experienced abuse, neglect, or exploitation, NACCER offers them a second chance at life, filled with love, support, and opportunities for healing. Through its comprehensive approach to rehabilitation and prevention, NACCER not only transforms individual lives but also strengthens families and fosters a culture of compassion and resilience.",
                "charity_id": 5 
            },
            {
                "beneficiary_name":" Mercy Mwende",
                "Beneficiary Story" :"Thanks to The Education for All Scholarship, James Mukami's dreams of pursuing higher education have become a reality. Growing up in a low-income household, James faced numerous obstacles on his path to academic success. However, with the support of the scholarship, he has been able to enroll in university and pursue his passion for computer science. The scholarship not only covers James's tuition fees but also provides him with mentorship and resources to excel in his studies. With determination and hard work, James is determined to make the most of this opportunity and build a better future for himself and his family. The Education for All Scholarship has not only transformed James's life but also empowered him to inspire others in his community to strive for academic excellence and pursue their dreams.",
                "charity_id": 7
            },
            {
                "Beneficiary Name": "Sarah Wambui",
                "Beneficiary Story": "Sarah Wambui's journey at The Royal Seed Orphanage is a testament to the transformative power of love and support. Orphaned at a young age and facing uncertain prospects, Sarah found solace and hope within the walls of The Royal Seed Orphanage. Here, she not only found a safe haven but also discovered a nurturing community that believed in her potential. With guidance from the dedicated staff and volunteers, Sarah flourished academically, emotionally, and socially. The Royal Seed Orphanage provided her with access to quality education, nutritious meals, and opportunities for personal growth. Today, Sarah is a confident and resilient young woman, ready to embark on new adventures and pursue her dreams. The Royal Seed Orphanage has not only given Sarah a second chance at life but also empowered her to create a brighter future for herself and inspire others with her resilience and determination.",
                "charity_id": 6
            },
            {
                "Beneficiary Name": "Daniel Ochieng",
                "Beneficiary Story": "Daniel Ochieng's journey with the Food for Education Organization-Kenya (FEOK) is a testament to the transformative impact of access to education and nutritious meals. Growing up in a disadvantaged community where daily meals were often a luxury, Daniel faced immense challenges in pursuing his education. However, with the support of FEOK's initiatives, his life took a positive turn. FEOK provided Daniel with daily nutritious meals at school, ensuring that hunger no longer hindered his ability to learn. Moreover, through FEOK's educational programs, Daniel received additional support, including textbooks, school supplies, and academic tutoring. With determination and perseverance, Daniel excelled in his studies and graduated at the top of his class. Today, he aspires to become a doctor and give back to his community. FEOK's commitment to providing food and education to children like Daniel has not only changed individual lives but also uplifted entire communities, breaking the cycle of poverty and empowering future generations to thrive.",
                "charity_id": 3
            },{
                 "Beneficiary Name":'Jane Wanjiku',
                 "Beneficiary Story":"Jane Wanjiku, a single mother from a rural village in Kiambu County, faced hardships providing for her family due to limited opportunities. Through Kiambu County Women's Association (KIACOWA), Jane received training in tailoring. With determination, she started her own business, creating garments and offering alteration services. With KIACOWA's support, Jane's business thrived, improving her family's livelihood. Today, Jane is a successful entrepreneur and an advocate for women's empowerment, inspiring others in her community. Thanks to KIACOWA, Jane's journey showcases the transformative impact of empowerment and community support.",
                 "charity_id": 10
            },
            {
                "Beneficiary Name": "John Kiprop",
                "Beneficiary Story":"John Kiprop, a father from Eldoret, faced a daunting diagnosis of cancer. With limited resources and overwhelming fear, he found solace and support through the MTRH Friends of Cancer Patients Support Group. With their guidance and assistance, John received vital resources and emotional support during his treatment at Moi Teaching and Referral Hospital. Today, John is a cancer survivor, grateful for the support that helped him navigate his journey with strength and resilience. His story is a testament to the impact of community support in the fight against cancer.",
                "charity_id": 11
            },
            {
                "beneficiary_name": "Amina Ali",
                "beneficiary_story": "Amina Ali, a young girl from a marginalized community, faced numerous challenges in accessing education. ChildFund Kenya stepped in to provide Amina with the necessary school supplies and support. Amina's academic performance improved significantly, and she began to excel in her studies. With ChildFund Kenya's ongoing support, Amina is now on track to complete her education and pursue her dreams. Her success story
                "charity_id": 20
            }   
             {
                "beneficiary_name": "Lilian Achieng",
                "beneficiary_story": "Lilian Achieng's life changed dramatically when she received support from the Habitat for Humanity. Living in substandard housing, Lilian and her three children faced numerous health and safety challenges. Habitat for Humanity built a new, secure home for Lilian, providing her family with a stable foundation. With a safe place to live, Lilian was able to focus on her job and her children's education, leading to significant improvements in their quality of life. This new home has not only given them security but also hope for a brighter future.",
                "charity_id": 22
             },
             {
                "beneficiary_name": "Moses Mwangi",
                "beneficiary_story": "Moses Mwangi, a farmer in rural Kenya, benefited greatly from the Africa Sand Dam Foundation's efforts. Struggling with water scarcity, Moses's crops often failed, leading to financial instability. The Foundation built a sand dam in his community, which provided a reliable source of water year-round. With access to water, Moses was able to irrigate his crops consistently, leading to bountiful harvests and improved income. This has not only transformed Moses's life but also enhanced food security in his community.",
                "charity_id": 24
             }, 
            {
                "beneficiary_name": "Nairobi Children's Home",
                "beneficiary_story": "The children at Nairobi Children's Home have seen remarkable improvements in their living conditions and opportunities for education, thanks to the generous donations and support from the community. With new facilities, better nutrition, and access to educational resources, the children are thriving. The support has not only provided for their immediate needs but has also given them hope for a brighter future.",
                "charity_id": 12
            },
            {
                "beneficiary_name": "Youth Empowerment Program",
                "beneficiary_story": "Through the Youth Empowerment Program run by Heshima Kenya, many young people have found a new direction in life. By offering vocational training and educational support, the program has helped youths gain skills and confidence to secure employment and become self-reliant. This initiative has significantly reduced the number of unemployed youths in the community, fostering a generation of empowered and responsible individuals.",
                "charity_id": 13
            },
            {
                "beneficiary_name": "Elderly Care Initiative",
                "beneficiary_story": "The Elderly Care Initiative by Concern Worldwide Kenya has made a profound difference in the lives of senior citizens in Kericho. By providing healthcare, nutritious meals, and social activities, the initiative has improved their quality of life and ensured they are not forgotten. The program has created a sense of belonging and community for the elderly, who now enjoy a dignified and comfortable life.",
                "charity_id": 14
            },
            {
                "beneficiary_name": "Clean Water Project",
                "beneficiary_story": "The Clean Water Project by Maji Milele in Machakos has transformed the community by providing access to safe and clean drinking water. With new water kiosks and community sanitation facilities, the project has drastically reduced waterborne diseases and improved overall health. The availability of clean water has also enabled children to attend school regularly, as they no longer need to spend hours fetching water.",
                "charity_id": 15
            },
            {
                "Beneficiary Name": "Amina Juma",
                "Beneficiary Story": "Amina Juma's life took a hopeful turn when she became a part of the Light of Hope Children's Home. Orphaned and vulnerable, Amina faced a bleak future. However, the compassionate care at the children's home provided her with a stable and loving environment. Through personalized attention and a focus on holistic development, Amina thrived academically and personally. The home ensured she had access to quality education, healthcare, and emotional support. Today, Amina is a university student studying social work, driven by a desire to help other children in need. The Light of Hope Children's Home not only gave Amina a second chance but also instilled in her the values of empathy and community service.",
                "charity_id": 7
            },
            {
                "Beneficiary Name": "Joseph Mwangi",
                "Beneficiary Story": "Joseph Mwangi's path changed significantly with the support of the Nairobi Community Development Initiative (NCDI). Growing up in the impoverished neighborhoods of Nairobi, Joseph faced numerous challenges, including lack of access to basic necessities and education. NCDI's intervention provided him with scholarships, mentorship, and essential life skills training. This support enabled Joseph to complete his secondary education and enroll in a technical college, where he is now pursuing a diploma in electrical engineering. Joseph's success story is a powerful example of how targeted community development programs can break the cycle of poverty and create lasting change.",
                "charity_id": 8
            },
            {
                "Beneficiary Name": "Mary Atieno",
                "Beneficiary Story": "Mary Atieno, a widow with three children, found herself struggling to provide for her family after the loss of her husband. The Women for Women Empowerment Organization (WFWEO) stepped in, offering Mary vocational training in baking and small business management. With their guidance, Mary started a successful bakery business in her community. Her newfound skills and confidence not only improved her family's financial stability but also allowed her to become a role model for other women facing similar hardships. Today, Mary employs several women in her bakery, promoting economic empowerment and self-reliance within her community.",
                "charity_id": 9
            },
            {
                "Beneficiary Name": "Peter Njoroge",
                "Beneficiary Story": "Peter Njoroge's life was transformed by the Kenya Children’s Fund (KCF). Abandoned at a young age, Peter was living on the streets, facing daily hardships and dangers. KCF rescued him, providing a safe home and access to education. With the support of caring mentors and teachers, Peter excelled in school and discovered his passion for music. KCF nurtured his talent, and today, Peter is a promising musician, using his art to inspire and uplift others. His journey from the streets to a hopeful future highlights the critical role of compassionate interventions in changing the lives of vulnerable children.",
                "charity_id": 12
            },
            {
                "Beneficiary Name": "Fatuma Abdallah",
                "Beneficiary Story": "Fatuma Abdallah's struggle with chronic illness made everyday life a challenge. Living in a remote village with limited access to healthcare, she often felt isolated and hopeless. The Healthcare Access Project (HAP) reached out to Fatuma, providing her with regular medical check-ups, medication, and health education. The consistent medical care significantly improved her quality of life. Fatuma is now able to manage her condition effectively and actively participate in community activities. Her story demonstrates the profound impact of accessible healthcare services on individual well-being and community vitality.",
                "charity_id": 13
            },
            {
                "Beneficiary Name": "Grace Muthoni",
                "Beneficiary Story": "Grace Muthoni's life took a positive turn when she joined the Brighter Futures Initiative (BFI). Growing up in a marginalized community with limited access to education, Grace faced significant barriers to realizing her potential. However, BFI's scholarship program provided her with the opportunity to attend school and pursue her dreams. With determination and hard work, Grace excelled academically and became the first person in her family to graduate from university. Today, she works as a teacher, inspiring other young girls to pursue education and break free from the cycle of poverty. Grace's journey exemplifies the transformative power of education and the importance of investing in the future of marginalized youth.",
                "charity_id": 14
            },
            {
                "Beneficiary Name": "Sophia Chepkoech",
                "Beneficiary Story": "Sophia Chepkoech's journey with the Rural Women's Empowerment Initiative (RWEI) is a testament to the resilience of women in rural areas. As a young widow struggling to provide for her children, Sophia faced numerous challenges, including lack of access to financial resources and market opportunities for her agricultural products. RWEI provided her with training in modern farming techniques, access to microloans, and links to local markets. With determination and the support of RWEI, Sophia transformed her small farm into a thriving enterprise, becoming a successful agripreneur in her community. Today, she mentors other women, sharing her knowledge and empowering them to achieve economic independence. Sophia's story highlights the critical role of women's empowerment initiatives in building sustainable rural economies.",
                "charity_id": 16
            },
            {
                "Beneficiary Name": "Elijah Musyoka",
                "Beneficiary Story": "Elijah Musyoka's life was marred by substance abuse until he found hope through the Hope and Recovery Center (HRC). Battling addiction and mental health issues, Elijah struggled to maintain stable employment and relationships. HRC provided him with comprehensive rehabilitation services, including counseling, detoxification, and vocational training. With the support of HRC's dedicated staff, Elijah successfully completed his treatment and transitioned to independent living. Today, he works as a peer counselor at HRC, offering guidance and support to others on the path to recovery. Elijah's journey is a testament to the transformative power of rehabilitation and the importance of community-based mental health services.",
                "charity_id": 17
            },
            {
                "Beneficiary Name": "David Kimani",
                "Beneficiary Story": "David Kimani's life was forever changed by the intervention of the Urban Youth Empowerment Program (UYEP). Born and raised in a crime-ridden neighborhood, David faced pressure to join local gangs and engage in illegal activities. UYEP provided him with an alternative path through mentorship, vocational training, and job placement services. David discovered a passion for carpentry and, with UYEP's support, started his own furniture-making business. He now employs other at-risk youth from his community, offering them a chance to rebuild their lives. David's story illustrates the transformative impact of providing opportunities and support to disadvantaged youth, empowering them to become agents of positive change.",
                "charity_id": 15
            },
            {
                "Beneficiary Name": "Youth for Change",
                "Beneficiary Story": "Youth for Change is a youth-led movement dedicated to promoting social justice, equality, and human rights in local communities. Through advocacy campaigns, educational workshops, and community service projects, young people are mobilized to address pressing issues such as gender inequality, racial discrimination, and access to education. By empowering youth to become agents of change, Youth for Change inspires a new generation of leaders committed to building a more just and equitable society. Their collective efforts demonstrate the power of youth activism in driving positive social change.",
                "charity_id": 23
            },
            {
                "Beneficiary Name": "Peter Omondi",
                "Beneficiary Story": "Peter Omondi, a young student from a disadvantaged background, dreamt of pursuing higher education but lacked the financial means to do so. Through the Education for All Scholarship Fund, Peter was awarded a scholarship that covered his tuition fees and living expenses. With access to quality education, Peter excelled academically and graduated with honors. Today, he works as a teacher, inspiring other young people to pursue their dreams. Peter's story illustrates the life-changing impact of scholarships in unlocking the potential of bright and motivated students from underserved communities.",
                "charity_id": 7
            },
            {
                "Beneficiary Name": "Grace Achieng",
                "Beneficiary Story": "Grace Achieng, a single mother living in a Nairobi slum, faced numerous challenges in providing for her children. With support from the Western Kenya Community Driven Development and Flood Mitigation Project, Grace received training in tailoring and started her own small business. Through hard work and determination, Grace expanded her business and improved her family's living conditions. Today, she is a role model in her community, inspiring other women to pursue their entrepreneurial dreams. Grace's journey highlights the power of community-driven initiatives in empowering individuals to break the cycle of poverty and build better futures for themselves and their families.",
                "charity_id": 22
            },
            {
                "Beneficiary Name": "Lucy Chepkoech",
                "Beneficiary Story": "Lucy Chepkoech, a talented athlete from a rural village in Kenya, faced numerous obstacles in pursuing her passion for running. With support from the Rural Water and Sanitation Support Programme (RWASSP), Lucy gained access to clean water and sanitation facilities, improving her health and well-being. With renewed energy and determination, Lucy trained tirelessly and eventually represented her country in international competitions. Today, she is a celebrated athlete and a source of inspiration for young girls across Africa. Lucy's journey exemplifies the transformative power of access to basic amenities in unlocking individual potential and achieving dreams.",
                "charity_id": 20
            }















        ]
        for story_data in stories_data:
            story = Story(**story_data)
            db.session.add(story)
        db.session.commit()
       
    create_admin()
    create_donor_seed()
    create_charities()
    seed_stories()

    print('Complete!')
