from __future__ import annotations

from http import HTTPStatus
from typing import List

import edgedb
from fastapi import APIRouter, Depends, HTTPException, Query
from pydantic import BaseModel


router = APIRouter()

