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
        admin.username = "admin"
        admin.password_hash = "your_password"
        db.session.add(admin)
        db.session.commit()


    def create_charities():
        charities_data = [
            {
                "title": "Kenya Red Cross Society",
                "charity_description": "The Kenya Red Cross Society (KRCS) is a non-governmental organization that works in the humanitarian field. It was founded in 1960 and is part of the International Federation of Red Cross and Red Crescent Societies. Its main goal is to help people affected by disasters or conflicts, like floods, droughts, or famines.",
                "organizer_name": "Kennedy Omunga",
                "location": "Nairobi",
                "period": "1965-12-21",
                "status": "Active",
                "total_amount": 10000000
            },
            {
                "title": " Heshima Kenya",
                "charity_description": "Heshima Kenya is a non-profit organization that works with children affected by HIV and AIDS. The organization provides education, food, clothing, and medical care to children who have lost their parents to AIDS.",
                "organizer_name": "Philip Karanja",
                "location": "Nairobi",
                "period": "2008-01-12",
                "status": "Active",
                "total_amount": 400000
            },
            {
                "title": " Food for Education Organization-Kenya(FEOK)",
                "charity_description": "FEOK is a non-governmental organization that aims to provide food and education to children in Kenya. The main objective is to provide meals for children from low-income families so they can attend school regularly. It also aims to improve nutritional status, physical growth, and cognitive development.",
                "organizer_name": "Caren Chebet",
                "location": "Kisumu",
                "period": "2012-09-20",
                "status": "Active",
                "total_amount": 5000
            },
            {
                "title": "Nakuru Children’s Rescue and Rehabilitation Centre (NACCER)",
                "charity_description": "Nakuru Children’s Rescue and Rehabilitation Centre (NACCER) is a non-profit organization that works to protect children from abuse, neglect, and exploitation. NACCER provides a safe home for children who have been abused, abandoned, or neglected. They also work with the community to prevent abuse and neglect by offering health education programs, workshops on parenting skills, and counseling services.",
                "organizer_name": "Karanja Wamwega",
                "location": "Nakuru",
                "period": "2004-07-02",
                "status": "Active",
                "total_amount": 60000
            },
            {
                "title": "Ebenezer Foundation",
                "charity_description": "Ebenezer Christian Children’s Home was founded in 1994 as an avenue to provide a loving, Christian environment to children removed from their homes due to neglect or abuse. ECCH is a fully licensed North Carolina Residential Child-Care Facility, and a 501 (c)(3) nonprofit organization. Ebenezer Christian Children’s Home believes that God has called us to continually share Christ’s love with all those who pass our way. We seek to minister to the spiritual, physical, emotional, and educational needs of the children that have been placed in our care. ",
                "organizer_name": "Barry Byrd",
                "location": "North California",
                "period": "1994-06-22",
                "status": "Active",
                "total_amount": 50000
            },
            {
                "title": " The Royal Seed Orphanage",
                "charity_description": "The Royal Seed Orphanage has a team of dedicated volunteers who assist with day-to-day operations. They ensure that all children are cared for and given access to nutritious food and clean water. The orphanage also provides education and sports facilities for the children to grow up healthy and happy.",
                "organizer_name": "Purity Mukuba",
                "location": "Meru",
                "period": "1993- 09-28",
                "status": "Active",
                "total_amount": 30000
            },
            {
                "title": "The Education for All Scholarship ",
                "charity_description": "The Education for All Scholarship is a transformative initiative dedicated to providing financial support and educational opportunities to deserving students worldwide. By removing financial barriers, the scholarship empowers individuals to pursue their academic goals and unlock their full potential. Through its commitment to educational equity and inclusivity, the program strives to create a brighter future for all.",
                "organizer_name": " Dennis Ochieng",
                "location": "Kakamega",
                "period": "1978-08-03",
                "status": "Active",
                "total_amount": 300000
            }, 
            {
                "title": " Habitat for Humanity",
                "charity_description": "Habitat for Humanity works to build affordable housing and provide shelter to families in need around the world.",
                "organizer_name": "Jeff Clinton",
                "location": "Nairobi",
                "period": "2001-04-16",
                "status": "Active",
                "total_amount": 1200000
            },  
             {
            "title": "World Wildlife Fund (WWF)",
            "charity_description": "WWF is dedicated to conservation efforts to protect endangered species and their habitats, as well as promoting sustainable practices to address environmental challenges.",
            "organizer_name": "Organizer 2",
            "location": "Nairobi",
            "period": "1961-04-20",
            "status": "Active",
            "total_amount": 25000
        }, 
         {
            "title": "Kiambu County Women's Association (KIACOWA)",
            "charity_description": "KIACOWA is a local non-profit organization based in Kiambu County, Kenya, dedicated to empowering women and promoting community development. Founded by a group of passionate women leaders, KIACOWA focuses on various initiatives aimed at improving the lives of women, children, and families in the region. These initiatives may include skills training programs, economic empowerment projects, healthcare services, education support, and advocacy for women's rights and gender equality. Through its grassroots approach and community engagement, KIACOWA strives to address the unique challenges faced by women and vulnerable populations in Kiambu County, fostering sustainable development and positive social change.",
            "organizer_name": "Adena Kane",
            "location": "Kiambu",
            "period": "2010-02-04",
            "status": "Active",
            "total_amount": 100000
         },
         {{
            "title": "Moi Teaching and Referral Hospital (MTRH) Friends of Cancer Patients Support Group:",
            "charity_description": "The MTRH Friends of Cancer Patients Support Group is a community-based organization in Eldoret dedicated to providing support and assistance to cancer patients and their families. Through emotional support, counseling, financial aid, and advocacy efforts, the group aims to alleviate the burdens faced by cancer patients and improve their quality of life. By fostering community solidarity and raising awareness about cancer prevention and treatment, the group plays a vital role in empowering patients and promoting early detection.",
            "organizer_name": "Jediel Kiptum",
            "location": "Eldoret",
            "period": "1999 -04-21",
            "status": "Active",
            "total_amount": 7000000
        }
             
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
            {"firstname": "Todd ", "lastname": "Josh", "username": "todd", "password": "pass12334", "amount": 50000},
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