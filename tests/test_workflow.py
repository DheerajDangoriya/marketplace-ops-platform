# Fixed: removed the extra "_workflow"
from app.services.workflow import run_workflow

def test_workflow_runs_without_errors():
    run_workflow()
    assert True