Social Network App
https://chatgpt.com/c/67735bc1-9774-8012-96f6-d794d706a97a

A. Phase I - Requirement (Inception):
I. Users (Actor):
1/ Admin
2/ Registered User
3/ Guest(optional)
4/ Business Partners 


II. Use cases (Elaboration):
1. Use Cases List:
2. Use Cases Diagram:
3. Requirement Document: Detailed Use Cases 

B. Phase II - Architecture and the Designs:
I. Architecture:
1. Application architechture
2. System architechture
3. Data architechture
4. UX (User experience) architechture 
5. Security architechture(optional)

II. Phase II - Designs:
1. OOAD
2. Database
3. Infrastructure
4. Wireframe/ Mock screens
5. Security (optional)

C. Phase III - Construction:
1. Prototype
2. Develop-Integrate-Test

D. Phase IV - Deployment:
1. Testing
2. Deployment: Local/Cloud

---------------------------------------------------------------------------------------------------------------------------------------------------------
A. Phase I - Requirement (Inception):
I. Users (Actor):

1/ Admin: 
2/ Moderators: 
3/ User:
4/ Business Partners :
6/ Groups:

II. Use cases (Elaboration):

1. Use Cases List:(28)
    - Admin:  manage users, set/enforce community behavior rules/ standards, analyze users behavior(AI) , introduce features
    - Moderators: moderate contents, handle violations, filter hate speech(AI)
    - Personal:  create Posts, read posts in joint groups publicly/ friend/ private , add friends,  share photos/ posts, reply with comments, react to post,  join groups, 
    create personal events, chat with friends, watch 30-sec videos, buy/sell products, recommend friends/ connections(AI), news feed (AI), personal chatbot (AI), follow person,
    - Group: create group, manage group users, accept new member, earn and monetize through Social Donation, 
    - Business: create ads locally/ globally, monitor and analyze ad performance, audience segmentation(AI)

    Iteration 1: 
    Admin: manage users(UC10)
    Moderators: filter hate speech(AI) (UC11)
    Personal: register self-user(UC01) create posts in public/ friend/ private(UC02), read posts (UC03), add friends(UC04), react to post(UC05),reply with comments(UC09)
    Group: create group(UC06), manage group users(UC07), accept new member(UC08)
    
2. Use Cases Diagram:
3. Requirement Document: Detailed Use Cases:

      UC04-Friends Management:
        Send Friend Request, Accept Friend Request, Decline Friend Request, Cancel Friend Request, Unfriend, List friends, share (posts), request lists (send, receive)
        requested_at time, friended_at time, status: pending, accepted, rejected, cancelled, deleted
        Profile & Post Visibility – A user can choose who among their friends can see certain posts.
        Tagging in Posts & Comments – Users can tag friends in posts, comments, and photos. 
        Reactions & Comments – Friends can like, comment, and react to each other's posts.
        Later: Friend Suggestions – Facebook recommends new friends based on mutual friends and interactions.f






B. Phase II - Architecture and the Designs:
I. Architecture:
Technology stack:
    1. Front-end: React, Bootstrap, Redux
    2. Back-end: Python/ Java, Django/Flask or SpringBoot, Rest APIs, microservice, KafkaMQ
    3. Database: Mysql, Cassandra, Redis  
1. Application architechture:
- Django: URL -> View -> Model -> Template
2. System architechture
3. Data architechture
4. UX (User experience) architechture 
5. Security architechture(optional)


