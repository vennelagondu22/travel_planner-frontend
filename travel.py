import gradio as gr
import requests
import os

FASTAPI_URL="https://travel-planner-backend-82es.onrender.com/plan_trip"

def get_plan(destination, days, budget, interests):
    try:
        response = requests.get(
            FASTAPI_URL,
            params={
                "destination": destination,
                "days": days,
                "budget": budget,
                "interests": interests
            }
        )
        response.raise_for_status()
        data = response.json()
        return f"""
        Destination: {data['destination']}
        Days: {data['days']}
        Budget: {data['budget']}
        
        🗓️ Itinerary:
        {data['itinerary']}
        """
    except Exception as e:
        return f"❌ Error: {str(e)}"

demo = gr.Interface(
    fn=get_plan,
    inputs=[
        gr.Textbox(label="Destination"),
        gr.Slider(1, 14, label="Days"),
        gr.Slider(100, 50000, label="Budget"),
        gr.Textbox(label="Interests")
    ],
    outputs="text",
    title="🌍 AI Travel Planner (Gradio)",
    description="Generate personalized itineraries using Gemini + FastAPI"
)

if __name__ == "__main__":
    demo.launch(
        server_name="0.0.0.0",
        server_port=int(os.environ.get("PORT", 7860))
    )