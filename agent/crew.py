import streamlit as st
from crewai import Crew, Process
from tasks import research_task, write_task
from agent import news_researcher, news_writer

# Streamlit app
def main():
    st.title("Tech-Focused Crew Task Execution")

    st.header("Forming the Tech-Focused Crew with Enhanced Configuration")
    topic = st.text_input("Enter the topic for research:")

    if st.button("Start Task Execution"):
        if topic:
            crew = Crew(
                agents=[news_researcher, news_writer],
                tasks=[research_task, write_task],
                process=Process.sequential,
            )
            
            with st.spinner('Executing tasks...'):
                result = crew.kickoff(inputs={'topic': topic})
            
            st.success("Task Execution Completed!")
            st.write("Result:")
            st.write(result)
        else:
            st.error("Please enter a topic before starting the task execution.")

if __name__ == "__main__":
    main()
