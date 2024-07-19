import gradio as gr
from crewai import Crew, Process
from tasks import research_task, write_task
from agent import news_researcher, news_writer

def execute_task(topic):
    crew = Crew(
        agents=[news_researcher, news_writer],
        tasks=[research_task, write_task],
        process=Process.sequential,
    )
    result = crew.kickoff(inputs={'topic': topic})
    return result

# Gradio app
iface = gr.Interface(
    fn=execute_task,
    inputs=gr.Textbox(lines=2, placeholder="Enter the topic for research here..."),
    outputs="text",
    title="Tech-Focused Crew Task Execution",
    description="Forming the Tech-Focused Crew with Enhanced Configuration. Enter a topic to start the task execution process.",
)

iface.launch()
