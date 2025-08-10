_Search_ _[Write](https://medium.com/new-story?source=post_page---top_nav_layout_nav-----------------------------------------)_





|Home<br>Library<br>Profile<br>Stories<br>Stats<br>Following<br>NYU Center for Da…<br>ODSC - Open Data …<br>Fareed Khan<br>The Medium Blog<br>Dimitris Poulopoulos<br>Graham Harrison<br>Discover more writers<br>and publications to<br>follow.<br>See suggestions|Towards AI|
|---|---|
|_Following_<br>_Discover more writers_<br>_and publications to_<br>_follow._<br>_See suggestions_<br>_Home_<br>_Library_<br>_Profile_<br>_Stories_<br>_Stats_<br>_NYU Center for Da…_<br>_ODSC - Open Data …_<br>_Fareed Khan_<br>_The Medium Blog_<br>_Dimitris Poulopoulos_<br>_Graham Harrison_|_Member-only story_<br>**_Building AI Workflows with FastAPI_**<br>**_and LangGraph (Step-by-Step_**<br>**_Guide)_**<br>_GenAI Lab_<br>_Follow_<br>_4 min read · Jul 31, 2025_<br>_287_<br>_10_<br>_The leading AI_<br>_community and_<br>_content platform_<br>_focused on making AI_<br>_accessible to all. Check_<br>_out our new course_<br>_platform:_<br>_https://academy.toward_<br>_sai.net/courses/beginn_<br>_er-to-advanced-llm-_<br>_dev_<br>_Follow publication_<br>4FastAPl+<br>=AIAPIs<br>LangGraph|


Large Language Models (LLMs) are great at reasoning, but real-world


applications often require stateful, multi-step workflows. That’s where


LangGraph comes in — it lets you build intelligent workflows using graphs


of LLM-powered nodes.


But what if you want to expose these workflows as APIs, so other apps (or


users) can call them? That’s where FastAPI comes in — a lightweight, high

performance Python web framework.


In this guide, you’ll learn how to wrap a LangGraph workflow inside FastAPI


and turn it into a production-ready endpoint.


_**Why LangGraph + FastAPI?**_


LangGraph: Create multi-step, stateful workflows with LLMs (e.g., multi

agent reasoning, data processing).


FastAPI: Easily expose these workflows as REST APIs for integration with


web apps, microservices, or automation pipelines.


Together: Build scalable AI agents that can be accessed from anywhere.


_**1. Project Setup**_


Create a new project folder and install dependencies:





Create a .env file to store your API keys:





_**2. Building a Simple LangGraph Workflow**_


Let’s build a simple LangGraph that takes a user question and returns an AI

generated answer.





This graph:


1. Receives user_input


2. Sends it to GPT-4o


3. Returns the AI-generated response


_**3. Making It Production-Ready**_


Before exposing this to the world, let’s harden it for real use cases.


_**Error Handling & Retries**_


LLM APIs can fail or timeout. Wrap the call in try/except :





_**Input Validation**_


We don’t want someone sending huge payloads. Add Pydantic constraints:


_**Logging**_


Add logging for visibility:





_**4. Exposing the Workflow with FastAPI**_


Now, let’s wrap this workflow inside FastAPI.







Run the server:





_**5. Testing the API**_


curl :
You can test it using





Or open http://127.0.0.1:8000/docs in your browser — FastAPI auto

generates Swagger UI for you!













_This interactive UI lets you test your endpoint directly in the browser._





_**6. Scaling & Deployment**_


A few steps to prepare for production:


Async execution: FastAPI is async-native. For multiple LLM calls, make


functions async.


Workers: Run with multiple processes for concurrency:





Dockerization:





Authentication: Use API keys or JWT tokens to protect endpoints (Part 2


coming soon).


_**7. Architecture Overview**_


Here’s how it all connects:





This simple architecture lets you turn any LangGraph into an API.


_**6. Conclusion**_


In just a few steps, we:


Built a LangGraph workflow


Exposed it as a REST API using FastAPI


Added production-readiness features (validation, retries, logging)


Laid the foundation for scalable AI microservices


This setup can power anything from chatbots to document processors to AI


SaaS products.


What’s next?


I’m planning a Part 2 of this tutorial, but I want your input.


Which one would you like me to cover next?


1. Streaming responses (real-time chat)


2. Authentication & security


3. Docker & cloud deployment


4. Error monitoring & observability


Comment below with your pick!


_If you enjoyed this article and want more practical AI & LangGraph tutorials,_


_[follow GenAI Lab for weekly deep dives.](https://medium.com/genai-lab)_


_[Technology](https://medium.com/tag/technology?source=post_page-----599937ab84f3---------------------------------------)_ _[Artificial Intelligence](https://medium.com/tag/artificial-intelligence?source=post_page-----599937ab84f3---------------------------------------)_ _[Langchain](https://medium.com/tag/langchain?source=post_page-----599937ab84f3---------------------------------------)_ _[Langgraph](https://medium.com/tag/langgraph?source=post_page-----599937ab84f3---------------------------------------)_ _[Fastapi](https://medium.com/tag/fastapi?source=post_page-----599937ab84f3---------------------------------------)_


_287_ _10_



_Published in Towards AI_


_[85K followers · Last published 15 hours ago](https://medium.com/towards-artificial-intelligence/followers?source=post_page---post_publication_info--599937ab84f3---------------------------------------)_


_The leading AI community and content platform focused on making AI_

_accessible to all. Check out our new course platform:_

_[https://academy.towardsai.net/courses/beginner-to-advanced-llm-dev](https://academy.towardsai.net/courses/beginner-to-advanced-llm-dev)_


_Written by GenAI Lab_


_[311 followers · 8 following](https://medium.com/@genai-lab/followers?source=post_page---post_author_info--599937ab84f3---------------------------------------)_


_At GenAI Lab, practical implementations, code notebooks, and insights on the_

_latest AI advancements will be shared to help you turn ideas into innovation._


_Responses (10)_


_Luther_


_What are your thoughts?_


_[dilip kumar](https://medium.com/@dilipkumar2000.r?source=post_page---post_responses--599937ab84f3----0-----------------------------------)_

_[6 days ago](https://medium.com/@dilipkumar2000.r/authentication-from-the-ground-tjhough-it-would-be-great-if-you-used-this-instance-itself-as-an-1b7b76fbaac6?source=post_page---post_responses--599937ab84f3----0-----------------------------------)_



_Follow_


_Follow_



_authentication from the ground tjhough,it would be great if you used this instance itself as an example._



_93_



_Reply_


_[Darren Addy](https://medium.com/@darrenaddy?source=post_page---post_responses--599937ab84f3----1-----------------------------------)_

_[6 days ago](https://medium.com/@darrenaddy/step-by-step-instructions-of-a-workflow-workflow-taking-a-question-returning-an-answer-649243f6737d?source=post_page---post_responses--599937ab84f3----1-----------------------------------)_



_Step by Step Instructions of a workflow_


_Workflow = Taking a question & returning an answer?_



_33_



_1 reply_ _Reply_


_[Dugasanisatish](https://medium.com/@dugasanisatish?source=post_page---post_responses--599937ab84f3----2-----------------------------------)_

_[6 days ago](https://medium.com/@dugasanisatish/authentication-security-374793a31494?source=post_page---post_responses--599937ab84f3----2-----------------------------------)_



_Authentication & security_



_88_



_Reply_



_See all responses_


_[More from the list: "Reading list"](https://medium.com/@lutherremote/list/reading-list?source=post_page---list_recirc--599937ab84f3-----------predefined%3Aa1ffd95fa01e%3AREADING_LIST----------------------------)_


_[Curated by Luther](https://medium.com/@lutherremote?source=post_page---list_recirc--599937ab84f3-----------predefined%3Aa1ffd95fa01e%3AREADING_LIST----------------------------)_



_[Level Up…](https://medium.com/gitconnected?source=post_page---list_recirc--599937ab84f3-----------predefined%3Aa1ffd95fa01e%3AREADING_LIST----------------------------)_ _by_ _[Gaurav S…](https://medium.com/@gaurav21s?source=post_page---list_recirc--599937ab84f3-----------predefined%3Aa1ffd95fa01e%3AREADING_LIST----------------------------)_ _[Kalash Vasaniya](https://medium.com/@kalashvasaniya1?source=post_page---list_recirc--599937ab84f3-----------predefined%3Aa1ffd95fa01e%3AREADING_LIST----------------------------)_ _In_ _[Agentic AI & G…](https://medium.com/generative-ai-revolution-ai-native-transformation?source=post_page---list_recirc--599937ab84f3-----------predefined%3Aa1ffd95fa01e%3AREADING_LIST----------------------------)_ _by_ _Y…_ _[Gary Svenson](https://medium.com/@garysvenson09?source=post_page---list_recirc--599937ab84f3-----------predefined%3Aa1ffd95fa01e%3AREADING_LIST----------------------------)_ _In_ _[Everyd…](https://medium.com/everyday-ai?source=post_page---list_recirc--599937ab84f3-----------predefined%3Aa1ffd95fa01e%3AREADING_LIST----------------------------)_ _by_ _[M](https://medium.com/@singh.manpreet171900?source=post_page---list_recirc--599937ab84f3-----------predefined%3Aa1ffd95fa01e%3AREADING_LIST----------------------------)_







_In_ _[Everyd…](https://medium.com/everyday-ai?source=post_page---list_recirc--599937ab84f3-----------predefined%3Aa1ffd95fa01e%3AREADING_LIST----------------------------)_ _by_







_**WhatsApp MCP A**_
_**That Work While**_


_·_
_Apr 2_







_[View list](https://medium.com/@lutherremote/list/reading-list?source=post_page---list_recirc--599937ab84f3-----------predefined%3Aa1ffd95fa01e%3AREADING_LIST----------------------------)_


_More from GenAI Lab and Towards AI_



_In_ _[Towards AI](https://medium.com/towards-artificial-intelligence?source=post_page---author_recirc--599937ab84f3----0---------------------d054f285_d75b_46e8_aea1_c6b19c8a7ad0--------------)_ _by_ _[GenAI Lab](https://medium.com/@genai-lab?source=post_page---author_recirc--599937ab84f3----0---------------------d054f285_d75b_46e8_aea1_c6b19c8a7ad0--------------)_


_**LangGraph Introduction: Building**_
_**Intelligent Workflows with OpenAI**_


_Introduction_



_**I used MCP for 3 months:**_

_**Everything You Need to Know + 2…**_


_MCP client configs & workarounds, servers,_
_proxy DevTools. Find & install. Top MCP…_



_In_ _[Towards AI](https://medium.com/towards-artificial-intelligence?source=post_page---author_recirc--599937ab84f3----1---------------------d054f285_d75b_46e8_aea1_c6b19c8a7ad0--------------)_ _by_ _[Damien Berezenko](https://medium.com/@qdrddr?source=post_page---author_recirc--599937ab84f3----1---------------------d054f285_d75b_46e8_aea1_c6b19c8a7ad0--------------)_



_Jul 18_



_3_



_Jul 5_



_728_ _3_



_In_ _[Towards AI](https://medium.com/towards-artificial-intelligence?source=post_page---author_recirc--599937ab84f3----2---------------------d054f285_d75b_46e8_aea1_c6b19c8a7ad0--------------)_ _by_ _[MahendraMedapati](https://medium.com/@mahendramedapati?source=post_page---author_recirc--599937ab84f3----2---------------------d054f285_d75b_46e8_aea1_c6b19c8a7ad0--------------)_



_**The Ultimate Guide to Agentic**_
_**AI Frameworks in 2025: Which O…**_


_—_
_From zero to AI agent hero_ _the complete_
_roadmap that 10,000+ developers are using…_



_In_ _[Towards AI](https://medium.com/towards-artificial-intelligence?source=post_page---author_recirc--599937ab84f3----3---------------------d054f285_d75b_46e8_aea1_c6b19c8a7ad0--------------)_ _by_ _[GenAI Lab](https://medium.com/@genai-lab?source=post_page---author_recirc--599937ab84f3----3---------------------d054f285_d75b_46e8_aea1_c6b19c8a7ad0--------------)_


_**Google’s A2A Protocol: A New**_
_**Standard for Agent-to-Agent…**_


_AI agents are no longer isolated experiments_

_—_
_they’re evolving into complex ecosystems…_



_Jul 25_



_335_ _11_



_6d ago_



_43_



_[See all from GenAI Lab](https://medium.com/@genai-lab?source=post_page---author_recirc--599937ab84f3---------------------------------------)_ _[See all from Towards AI](https://medium.com/towards-artificial-intelligence?source=post_page---author_recirc--599937ab84f3---------------------------------------)_


_Recommended from Medium_


_[Shravan Kumar](https://medium.com/@shravankoninti?source=post_page---read_next_recirc--599937ab84f3----0---------------------5181a9e8_96aa_48a6_960b_11a5f9c83fb6--------------)_


_**Build a Small Language Model**_
_**(SLM) From Scratch**_


_At this current phase of AI evolution, any_
_model with fewer than 1 billion parameters…_



_[GANTEDA RAJABABU](https://medium.com/@john011334?source=post_page---read_next_recirc--599937ab84f3----1---------------------5181a9e8_96aa_48a6_960b_11a5f9c83fb6--------------)_


_**Transforming Unstructured Text**_
_**into Interactive Knowledge Graph…**_


_Introduction_



_Jul 25_



_162_ _8_



_Jul 24_



_180_ _3_



_In_ _[Data Science Collective](https://medium.com/data-science-collective?source=post_page---read_next_recirc--599937ab84f3----0---------------------5181a9e8_96aa_48a6_960b_11a5f9c83fb6--------------)_ _by_ _[Ida Silfverskiöld](https://medium.com/@ilsilfverskiold?source=post_page---read_next_recirc--599937ab84f3----0---------------------5181a9e8_96aa_48a6_960b_11a5f9c83fb6--------------)_


_**Agentic AI: Working with Evals**_


_What we did before and what we do now_



_In_ _[AIGuys](https://medium.com/aiguys?source=post_page---read_next_recirc--599937ab84f3----1---------------------5181a9e8_96aa_48a6_960b_11a5f9c83fb6--------------)_ _by_ _[Vishal Rajput](https://medium.com/@vishal-ai?source=post_page---read_next_recirc--599937ab84f3----1---------------------5181a9e8_96aa_48a6_960b_11a5f9c83fb6--------------)_


_**Leave Agentic AI Frameworks And**_
_**Build Agents From Scratch**_


_I’ll be honest with you, I hate most agent-_
_based AI workflows; they are simply unusabl…_



_2d ago_


_[Jannis](https://medium.com/@PowerUpSkills?source=post_page---read_next_recirc--599937ab84f3----2---------------------5181a9e8_96aa_48a6_960b_11a5f9c83fb6--------------)_



_314_ _4_



_4d ago_



_639_ _24_



_**Google Just Eliminated the AI**_
_**Infrastructure Headache for…**_


_Google just solved the biggest pain point for_
_developers building AI solutions: the…_



_[Ramakrushna Mohapatra](https://medium.com/@techwithram?source=post_page---read_next_recirc--599937ab84f3----3---------------------5181a9e8_96aa_48a6_960b_11a5f9c83fb6--------------)_


_**Top 10 LLM & RAG Projects for Your**_

_**–**_
_**AI Portfolio (2025**_ _**26)**_


_Retrieval-Augmented Generation (RAG) is_
_like giving your AI a memory upgrade and a…_



_Aug 2_



_1.2K_ _19_



_Aug 3_



_282_ _8_



_[See more recommendations](https://medium.com/?source=post_page---read_next_recirc--599937ab84f3---------------------------------------)_


_[Help](https://help.medium.com/hc/en-us?source=post_page-----599937ab84f3---------------------------------------)_ _[Status](https://medium.statuspage.io/?source=post_page-----599937ab84f3---------------------------------------)_ _[About](https://medium.com/about?autoplay=1&source=post_page-----599937ab84f3---------------------------------------)_ _[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----599937ab84f3---------------------------------------)_ _[Press](mailto:pressinquiries@medium.com)_ _[Blog](https://blog.medium.com/?source=post_page-----599937ab84f3---------------------------------------)_ _[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----599937ab84f3---------------------------------------)_ _[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----599937ab84f3---------------------------------------)_ _[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----599937ab84f3---------------------------------------)_ _[Text to speech](https://speechify.com/medium?source=post_page-----599937ab84f3---------------------------------------)_


