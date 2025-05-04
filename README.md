# OIM_3640_Final_Project
 Final Project repository for OIM 3640 courses. 
Group members:
    Dhiren Reddy
    Alexey Sarychev

# Project Proposal

## The Big Idea.

Telegram or messages (depending on ease of implementation) bot for Babson events that scrapes the belong website and sends automated messages twice a day – one with today’s events and the other one with upcoming events within the next two weeks. **The MVP would include a website that allows students to pick where they want to receive updates (email or phone number) and input their contact details, which are later stored in a database, and a python bot that sends automated updates about events today, upcoming events, and changes in the events.** The project can be later built upon to incorporate and automate other areas of Babson infrastructure, e.g., daily Trim menu updates, campus news, etc. Potential, but not very feasible, implementation of AI that uses Babson Student Portal to respond to more complicated requests, such as “send me a list of courses that count towards business analytics concentration”, or “what’s the phone number and address of Student Health Services?” (such interactive interface would only be possible with telegram or discord or directly implemented into the student portal and would require a direct collaboration with Babson). 

## Learning Objectives.

Alexey: I’m excited to learn more about python-telegram-bot implementation, and messaging automation through APScheduler. Additionally, I want to better my understanding of AI implementation through dotenv and different scraping libraries such as bs4. Our project might require storing data on our users such as their phone numbers and emails, if we decide to implement it through regular messaging, and in that case I’m excited to learn to store and pull data using csv in Python in order to make sure customers receive appropriate updates.  Overall, this project should be a great learning opportunity, it originally came from the Babo Bot, a SMS bot that used to update subscribers on the daily Trim menu, I hope what we build could serve the Babson community and be widely utilized by it, same as Babo Bot was. 

Dhiren: One of the few aspects of this course that I am excited to undertake is the use of web-scrapping technologies. This is mainly due to the fact that I have had technical experience with how web-scrappers work but I have never had the oppurtunity to implement my learnings into a tangible product. Thus, I hope that by undertkaing this project, not only will I understand the signficance of telegram bots for other activities (i.e. stock options/cryptocurrency) but I will also learn the back-end mechanisms required to ensure a feasible bot can be created. 
Lastly, I hope to use the project as a means to connect with the Babson community. From past experiences with products such as Babo bots, I have learnt the importance of creating viable products that ensure future generations of the Babson community are provided the adequate resources for success. As other programs have aided me throughout my college journey, I hope this project can replicate the same impacts as past college initiatives.

## Implementation Plan.

The first thing we need to do is set up and automate the regular scraping of Babson Belong for the events schedule using 'Beautiful Soup'/'requests'. We’ll have to figure out how to bypass the fact that only Babson students can access the Belong website and acquire the API if there is one. We need to store the data and update it regularly, which would be done through Google Sheets using their API. We need to make sure the data is formatted and stored smoothly. Then (in case it’s a telegram bot), we need to create a telegram bot and set up all of the potential commands, such as /events workshop, /events tomorrow. In case it is a messaging bot, we need to set up a website using HTML for people to submit their contact information and set up pathways for it to be stored securely. The email could be used to verify it is a Babson student is using the bot. We would also need to auto-categorize events based on keywords and improve the formatting for the bot. Finally, we deploy the bot and test, debug, and fix, before delivering the MVP.

## Project Schedule

Week 1 (13th April to 20th April): Finish setting up the scrapping bot (test, feasbility and final implementation must be finished within this time frame)
Week 2 (20th April to 27th April): Set up different command prompts that users can use (e.g /events workshop, /events tomorrow, /events finance). Improve code formatting and design the basics of the UX of the website. 
Week 3 (27th April to 3rd May): Creation of the website is finalized and the code is deployed to the cloud. FInal testings and iterations are performed during this week.

## Collaboration Plan

Due to different skillsets between both group members, the group has decided to undertake this project by segregating work based on the different skillsets present in the group. For instance, Dhiren has more experience with website creation as he has enrolled in the Babson web technologies course, and thus would be mainly tasked at developing the front-end of the project. Furthermore, as both group members have adequate experience with the use of APIs and web-scrapping, both members will be tasked with developing the backend of the project. This is necessary as the back end mechanism for the project can be considered the most important aspect of the project. 
In order to ensure effective collaboration and work flow between group members, it is necessary to establish an effective stream of communciation that will ensure that each group member is always aware of the task at hand as well as a method for problem solving. This is imperative as unepexcted problems that may hinder project progressions can be  prioritized and solved in an active manner. This issue is mitigated as not only has a direct communication stream been created via WhatsApp, but both members have similar schedules that allow for in-person meetings to happen on a weekly basis. Lastly, as both group members are closely associated withing the Babson atmosphere, direct communication is not only feasible but preferred between both group members. 

## Risks and Limitations

Based of external research into other projects and programs created by different students in different universtities one of the most prominent issues is the ability to scrape the .belong website that can only be accessed by Babson students. Our group must find a way to ensure that web-scrapping can occur effectively on this portal as not many past iterations have featued the .belong website. Furthermore, a means of communication with the Babson community must be established in order to ensure our target audience has access to our service/bot. 
Another issue at hand is the handling of phone numbers. More specifically, a SIM card may need to be purchased in order to send messages via the IOS messages app. Thus, a final decision into the project’s platform is still undeciided. Furthermore, there is ethical consierations with the storage of Babson students’ numbers and emails. An appropriate way must be formulated to ensure no ethical violations occur during our porject’s back-end mechanism.

## Additional Course Content

-	API keys and web-scrapping technology 
-	Use of html for website creation
-	Cloud management for user’s information (phone number and email address)

# Submission Reflection
To run the code just open telegram and find @evebabot and /start.

Based of the aforementioned proposal, changes were obligatory due to restrictions and obstacles the group faced during their submission. Our original intention was to create a web-scrapping bot that was able to send automated messages semi-daily regarding the ongoing campus events. However, we were not provided the access to the server (status code error: 403), thus rather than webscrapping technology, we came to the conclusion that .json files were required. Overall, we were able to extrapolate our idea and create mutliple commands (e.g. /events_today, /events_tomorrow, /events_date, /events_club and /events_type) that could access the .json files and provide users the filter lists of campus events. The .json file implemented into the project contains a list of all events conducted in the month of April that were manually inputted due to this unforeseen error. We had to use this method because there was no other way to scrape Babson websites. At some point we decided to pivot to a bot that instead outputs Trim menu based on commands such as /breakfast, /lunch and /dinner, but ran into 403 even on the dine-on-campus website. It is important to note that the group did not attempt to bypass the server as we warned by the Babson IT Centre that repercussion may be handed for these actions. So the bot is usable with accurate data if we were able to bypass the restriction and automate daily scraping. 

### Note 1
 The project submission deadline being towards the end of the academic year also contributed to our decision of mannually inputting data into a json file just to make sure the bot works, instead of scraping because there are simply no events in the end of the semester.  Thus, if /events_today returns "No events found 🎉", that's because there are no events, not because there are errors in the code or because we didn't automate scraping.  

### Note 2
Throughout the project multiple resources were utilized, including w3schools, pythonorg.docs, python-telegram-bot Docs, Python Dotenv Docs, and AI.

Lastly, the Telegram bot is a free to use bot that does not require authentication (i.e username and password) as it was against the Terms and Services of Belong to gain information regarding students. Despite these restrictions, the group wished to continue this project and thus manually inputting each data set was the best course of action.