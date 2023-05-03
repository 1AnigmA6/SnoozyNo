import streamlit as st

st.title("SnoozyNO")
st.header("A driver drowsiness system")

st.image("images\drivdrow.jpg")

st.subheader("Introduction")

st.markdown("""
Driving has become an essential skill to learn these days, as it supposes to be the most convenient way for people to travel from one place to another. Driving as important a skill, it requires the driver to be extremely focused, a high amount of multi-tasking and vigilance is essential. One of the biggest problem that arises is drowsiness and fatigue, this leads to a lowered sense of the surroundings and a very high reaction time to stimulus. This is one of the biggest reasons for fatalities every day and the number just keeps increasing. Drowsy driving is extremely risky where the drivers puts himself in risk and also others on road because of one’s simple mistake, it may cost a life of several other people.
Driver drowsiness has been a problem and the accidents caused due to it have been rising with time. It has been a risk to the driver and also the other vehicles. There has been no such solution yet available to the drivers around the world. With the rapid development in technology, I look to implement a project to alert the driver when he is feeling drowsy, making driving safer for the driver himself and all the others around him.
""")

st.subheader("How to use?")

st.markdown("""

1.	Click on the Detection tab on the site which leads you to the main interface where all main detection is done.
2.	Then select the alarm audio of your choice from the dropdown selectbox, you can also hear the sounds by simply clicking on them to check which of them suits you the best. Note: You are not allowed to proceed 	unless 	and until you select a sound.
3.	Now you are ready, as you want to start the detection you click on the button labeled as “Start Detection”.
4.	The webcam is displayed on the screen and takes constant readings, if you tend to be sleepy and your eyes close after a few seconds the alarm starts to ring. The alarm will wake you up.
5.	If your ride is over and you want to stop the process click on the button labeled “close” this will stop the system from taking readings.

""")

st.subheader("Statistics")

st.markdown("""
According to an article by medIndia:
1. 21 percent of all fatal accidents are due to drowsy driving.
2. 60 percent of adult drivers or about 168 million people have driven a vehicle while feeling drowsy in the past year.
3. About 37 percent or 103 million people have fallen asleep at the wheel, according to the National Sleep Foundation’s [NSF] 2005 poll.
4. 4 percent or approximately eleven million drivers admit they have had an accident or near accident because they dozed off or were too tired to drive.
5. Sleep-related crashes are most common in young people between the ages of 18 and 29.
6. The National Highway Traffic Safety Administration estimates that 100,000 accidents are the direct result of driver fatigue each year.

South Korean government records the cause of traffic accidents, 
""")
st.image("images\stats.png")

