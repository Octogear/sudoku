"""Auxiliary methods."""
import uuid


def gen_unique():
    """Generate unique 10 digits number and return str."""
    return str(uuid.uuid4())[:12]
