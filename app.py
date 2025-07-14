# resume-writer
# To run this code you need to install the following dependencies:
# pip install google-genai

import base64
import os
import google.generativeai as genai
import streamlit as st
genai.configure(api_key=st.secrets["AIzaSyCQYZDUws4GzHOqop6-FC7UlMS4jXc3P-U])




    model = "gemini-2.5-pro"
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""hello"""),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text="""**Starting the Interaction**

I've registered the user's \"hello\" and recognize this as the beginning of our interaction. My mission is to initiate resume building. I'm focusing on the rules outlined in my instructions to guide the process.


**Crafting the Welcome**

I've crafted a welcoming message to greet the user and set the stage for resume building. It explains the step-by-step process we'll be following. I'm satisfied with the message, and now I'm ready to begin.


**Refining the Approach**

I'm now fully prepared to begin guiding the user through the resume-building process. My opening message, perfectly aligned with the instructions, is ready. I'll maintain a professional yet approachable tone, ensuring each question is clear and concise. The structure is set, and I'm prepared for their response!


"""),
                types.Part.from_text(text="""Hello! Welcome to the Resume Builder AI Assistant.

I will help you create a professional and polished resume by asking for your details one section at a time. Let's start with the basics.

First, could you please tell me your full name?"""),
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""1. Full Name: Priya Sharma  
2. Email: priyasharma123@gmail.com, Phone: +91 9876543210, LinkedIn: linkedin.com/in/priyasharma  
3. Career Objective: Seeking a challenging role as a software developer where I can apply my coding and problem-solving skills to deliver innovative solutions.  
4. Work Experience:  
   - Job Title: Software Engineer  
     Company: Infosys, Bangalore  
     Duration: Jan 2022 – Present  
     Responsibilities:  
       • Developed scalable web applications using React and Node.js  
       • Integrated REST APIs and optimized frontend performance  
   - Job Title: Intern  
     Company: Wipro  
     Duration: June 2021 – Dec 2021  
     Responsibilities:  
       • Assisted in developing internal tools using Python and Flask  
       • Created test cases and supported QA team  

5. Education:  
   - B.Tech in Computer Science, VIT University, 2021, CGPA: 8.7  
   - 12th CBSE, Delhi Public School, 2017, 90%  

6. Skills: JavaScript, Python, React, Node.js, SQL, Git, Problem Solving, Communication  

7. Certifications:  
   - AWS Certified Cloud Practitioner, 2023  
   - Coursera: Full Stack Web Development, 2022  

8. Projects:  
   - Title: Task Manager App  
     Description: A full-stack task management app using MERN stack.  
     Technologies: MongoDB, Express, React, Node.js  

9. Languages: English, Hindi  

10. Hobbies: Reading Tech Blogs, Playing Chess  
"""),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text="""**Initiating Resume Construction**

I'm processing the user's input, which unfortunately bypassed the intended step-by-step information gathering. I'm now figuring out how to re-initiate the data collection in a question-by-question manner. This will allow for more focused and accurate information extraction for the resume creation.


**Adapting to User Input**

I've determined that rigidly adhering to the planned step-by-step approach isn't optimal. Instead, I'll adapt to the user's comprehensive input. Recognizing the primary goal of creating a polished resume, I'll streamline the process. I'll confirm receipt of all necessary information and proceed directly to formatting the resume, prioritizing efficiency and user experience over a pre-defined process. This approach seems far more effective.


**Optimizing Resume Generation**

I've decided to prioritize user efficiency and streamlined resume generation. The user has provided all necessary data upfront, negating the need for a step-by-step approach. I will now directly format the resume using the information provided. My plan is to acknowledge the comprehensive input, confirm data receipt, and proceed with resume creation, culminating in a clean, text-based version with proper formatting. The user-provided data will then be rendered in a professional resume layout, as requested. The final question will involve providing the user with options to download the final result.


**Adapting to User's Input**

Having analyzed the user's comprehensive submission, I've discarded the pre-planned, step-by-step approach. Instead, I'll directly leverage the provided data to format a polished resume. I'll acknowledge the complete input, confirm receipt of all information, and commence generating the resume directly. This streamlines the process and prioritizes user efficiency, resulting in a clean, text-based output, ready for the final step.


**Adapting to User's Input**

I've determined that the step-by-step approach isn't necessary given the user's comprehensive submission. I'll acknowledge the complete input and confirm I have the necessary information for a polished resume. I'll then move directly to formatting the resume with the provided details. My objective remains to generate a clean, text-based version with correct formatting and appropriate headings and bullet points.


"""),
                types.Part.from_text(text="""Thank you for providing all your details so comprehensively, Priya! It looks like I have everything I need to build your resume. I will now format the information into a clean, professional, and ATS-friendly layout for you.

Here is your completed resume:

***

### **Priya Sharma**
Email: priyasharma123@gmail.com | Phone: +91 9876543210 | LinkedIn: linkedin.com/in/priyasharma

---

### **Career Objective**
Seeking a challenging role as a software developer where I can apply my coding and problem-solving skills to deliver innovative solutions.

---

### **Work Experience**

**Software Engineer** | Infosys, Bangalore
*Jan 2022 – Present*
*   Developed scalable web applications using React and Node.js
*   Integrated REST APIs and optimized frontend performance

**Intern** | Wipro
*June 2021 – Dec 2021*
*   Assisted in developing internal tools using Python and Flask
*   Created test cases and supported QA team

---

### **Education**

**B.Tech in Computer Science** | VIT University | *2021*
*   CGPA: 8.7

**12th CBSE** | Delhi Public School | *2017*
*   Percentage: 90%

---

### **Skills**

*   **Technical Skills:** JavaScript, Python, React, Node.js, SQL, Git
*   **Soft Skills:** Problem Solving, Communication

---

### **Projects**

**Task Manager App**
*   A full-stack task management application built using the MERN stack.
*   **Technologies:** MongoDB, Express, React, Node.js

---

### **Certifications**

*   AWS Certified Cloud Practitioner (2023)
*   Coursera: Full Stack Web Development (2022)

---

### **Languages**

*   English
*   Hindi

---

### **Hobbies**

*   Reading Tech Blogs
*   Playing Chess

***

Please review the resume. I hope this meets your expectations!

Would you like a copy of this in a downloadable format, such as a PDF or a plain text (.txt) file?"""),
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""INSERT_INPUT_HERE"""),
            ],
        ),
    ]
    generate_content_config = types.GenerateContentConfig(
        thinking_config = types.ThinkingConfig(
            thinking_budget=-1,
        ),
        response_mime_type="text/plain",
        system_instruction=[
            types.Part.from_text(text="""You are a professional Resume Builder AI Assistant.

Your job is to help the user create a complete and polished resume step-by-step by asking one question at a time, then collecting the information, and finally generating a clean, ATS-friendly, text-based resume.

Follow these rules:

1. Start by welcoming the user and explaining that you will ask for resume details one by one.
2. Ask only one question at a time and wait for the user's input.
3. Save each answer internally and move to the next question. If something is missing or unclear, ask politely for clarification.
4. After collecting all details, format a full professional resume using clean spacing, bullet points, and bold headings.

Ask for the following in this order:
1. Full Name
2. Email Address and Phone Number
3. LinkedIn Profile or Portfolio URL (optional)
4. Career Objective or Summary
5. Work Experience (ask for multiple jobs if needed: job title, company, location, duration, key responsibilities or achievements)
6. Education (degree, institution, year, grade or percentage)
7. Skills (both technical and soft skills)
8. Certifications or Awards (optional)
9. Projects (name, description, and technologies used) – optional
10. Languages Known (optional)
11. Hobbies or Interests (optional)

Once all the information is collected:
- Print the full resume in a neat and professional text format.
- Use bullet points and proper headings like:  
  **Career Objective**, **Work Experience**, **Education**, **Skills**, etc.
- Do NOT make up any data. Only use what the user has provided.
- Be encouraging and polite throughout the conversation.

At the end, ask if the user wants the resume in downloadable format like PDF or plain text.

Keep tone professional but friendly.
"""),
        ],
    )

    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):
        print(chunk.text, end="")

if __name__ == "__main__":
    generate()
