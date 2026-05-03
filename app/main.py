from fastapi import FastAPI, Depends
from app.logging_config import logger
from sqlalchemy.orm import Session
from datetime import datetime
from app.database import Base, engine, get_db, SessionLocal
from app.services.workflow import run_workflow
from app.services import marketplace
from app.services.marketplace import update_order_status
from app.auth.routes import router as auth_router
from app.routes import order_routes
from app.models.order import OrderStatus
from app.models.user import User
from app.auth.utils import get_password_hash


app = FastAPI(title="Fulfillment Automation System")


# Create database tables on startup
@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)
    create_admin()


# Routers
app.include_router(auth_router)
app.include_router(order_routes.router)



@app.get("/")
def health_check():
    return {
        "status": "server is live",
        "timestamp": datetime.utcnow(),
        "service": "Marketplace Ops Platform",
        "version": "1.0.0"
    }


@app.get("/orders/new")
def get_new_orders(db: Session = Depends(get_db)):
    return marketplace.fetch_new_orders(db)


@app.post("/run")
def run(db: Session = Depends(get_db)):
    run_workflow(db)
    return {"message": "Workflow executed"}


@app.put("/orders/{order_id}/status")
def change_order_status(
    order_id: int,
    new_status: OrderStatus,
    db: Session = Depends(get_db)
):
    return update_order_status(db, order_id, new_status)


@app.get("/ping")
def ping():
    return {"message": "pong"}


# ---------- Create admin user safely ----------

def create_admin():
    db = SessionLocal()

    admin = db.query(User).filter(User.username == "admin").first()

    if not admin:
        admin_user = User(
            username="admin",
            hashed_password=get_password_hash("admin123"),
            role="admin"
        )

        db.add(admin_user)
        db.commit()

    db.close()