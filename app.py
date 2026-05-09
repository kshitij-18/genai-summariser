import gradio as gr
import requests

def summarize_text(text, max_length=150):
    """Summarize text using the Cloud Run API"""
    try:
        # Replace with your actual Cloud Run URL
        api_url = "https://your-cloud-run-url.a.run.app/summarize"
        response = requests.post(api_url, json={"text": text, "max_length": int(max_length)})
        if response.status_code == 200:
            return response.json()["summary"]
        else:
            return f"Error: {response.status_code}"
    except Exception as e:
        return f"Error: {str(e)}"

# Create Gradio interface
with gr.Blocks(title="GenAI Text Summarizer") as demo:
    gr.Markdown("# GenAI Text Summarizer")
    gr.Markdown("Enter text to get an AI-powered summary")

    with gr.Row():
        text_input = gr.Textbox(
            label="Input Text",
            placeholder="Paste your text here...",
            lines=10
        )

    with gr.Row():
        max_length = gr.Slider(
            minimum=50,
            maximum=300,
            value=150,
            step=25,
            label="Maximum Summary Length"
        )

    submit_btn = gr.Button("Summarize")

    output = gr.Textbox(
        label="Summary",
        lines=5,
        placeholder="Summary will appear here..."
    )

    submit_btn.click(
        fn=summarize_text,
        inputs=[text_input, max_length],
        outputs=output
    )

if __name__ == "__main__":
    demo.launch()