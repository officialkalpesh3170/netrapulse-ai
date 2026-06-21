from fastapi import FastAPI
app=FastAPI(
    title="NetraPulse AI Authentication Service",
    version="1.0.0",
    description="Authentication and Authorization Service for NetraPulse AI"
)

@app.get("/")
def root():
    return {
        "message":"NetraPulse AI Authentication Service Running"
        
    }