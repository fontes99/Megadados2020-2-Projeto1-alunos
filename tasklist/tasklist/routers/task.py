# pylint: disable=missing-module-docstring, missing-function-docstring, invalid-name
import uuid

from typing import Dict

from fastapi import APIRouter, HTTPException, Depends

from ..database import DBSession, get_db
from ..models import Task, User

router = APIRouter()

#================== CHAMADAS USER ==============================
@router.get(
    '/user',
    summary='Reads User list',
    description='Reads the whole User list.',
    response_model=Dict[uuid.UUID, User],
)
async def read_users(db: DBSession = Depends(get_db)):
    return db.read_users()

@router.post(
    '/user',
    summary='Creates a new user',
    description='Creates a new user and returns its UUID.',
    response_model=uuid.UUID,
)
async def create_user(user: User, db: DBSession = Depends(get_db)):
    return db.create_user(user)

@router.get(
    '/user/{uuid_}',
    summary='Reads user',
    description='Reads user from UUID.',
    response_model=User,
)
async def read_user(uuid_: uuid.UUID, db: DBSession = Depends(get_db)):
    try:
        return db.read_user(uuid_)
    except KeyError as exception:
        raise HTTPException(
            status_code=404,
            detail='User not found',
        ) from exception

@router.put(
    '/user/{uuid_}',
    summary='Replaces a user',
    description='Replaces a user identified by its UUID.',
)
async def replace_user(uuid_: uuid.UUID, item: User, db: DBSession = Depends(get_db)):
    try:
        db.replace_user(uuid_, item)
    except KeyError as exception:
        raise HTTPException(
            status_code=404,
            detail='User not found',
        ) from exception

@router.patch(
    '/user/{uuid_}',
    summary='Alters a user',
    description='Alter a user identified by its UUID.',
)
async def replace_user(uuid_: uuid.UUID, item: User, db: DBSession = Depends(get_db)):
    try:
        db.replace_user(uuid_, item)
    except KeyError as exception:
        raise HTTPException(
            status_code=404,
            detail='User not found',
        ) from exception

@router.delete(
    '/user/{uuid_}',
    summary='Deletes user',
    description='Deletes a user identified by its UUID',
)
async def remove_user(uuid_: uuid.UUID, db: DBSession = Depends(get_db)):
    try:
        db.remove_user(uuid_)
    except KeyError as exception:
        raise HTTPException(
            status_code=404,
            detail='user not found',
        ) from exception

@router.delete(
    '/user',
    summary='Deletes all users, use with caution',
    description='Deletes all users, use with caution',
)
async def remove_all_users(db: DBSession = Depends(get_db)):
    db.remove_all_users()


#================== CHAMADAS TASKS ==============================

@router.get(
    '',
    summary='Reads task list',
    description='Reads the whole task list.',
    response_model=Dict[uuid.UUID, Task],
)
async def read_tasks(completed: bool = None, db: DBSession = Depends(get_db)):
    return db.read_tasks(completed)

@router.post(
    '',
    summary='Creates a new task',
    description='Creates a new task and returns its UUID.',
    response_model=uuid.UUID,
)
async def create_task(item: Task, db: DBSession = Depends(get_db)):
    return db.create_task(item)


@router.get(
    '/{uuid_}',
    summary='Reads task',
    description='Reads task from UUID.',
    response_model=Task,
)
async def read_task(uuid_: uuid.UUID, db: DBSession = Depends(get_db)):
    try:
        return db.read_task(uuid_)
    except KeyError as exception:
        raise HTTPException(
            status_code=404,
            detail='Task not found',
        ) from exception


@router.put(
    '/{uuid_}',
    summary='Replaces a task',
    description='Replaces a task identified by its UUID.',
)
async def replace_task(
        uuid_: uuid.UUID,
        item: Task,
        db: DBSession = Depends(get_db),
):
    try:
        db.replace_task(uuid_, item)
    except KeyError as exception:
        raise HTTPException(
            status_code=404,
            detail='Task not found',
        ) from exception


@router.patch(
    '/{uuid_}',
    summary='Alters task',
    description='Alters a task identified by its UUID',
)
async def alter_task(
        uuid_: uuid.UUID,
        item: Task,
        db: DBSession = Depends(get_db),
):
    try:
        old_item = db.read_task(uuid_)
        update_data = item.dict(exclude_unset=True)
        new_item = old_item.copy(update=update_data)
        db.replace_task(uuid_, new_item)
    except KeyError as exception:
        raise HTTPException(
            status_code=404,
            detail='Task not found',
        ) from exception


@router.delete(
    '/{uuid_}',
    summary='Deletes task',
    description='Deletes a task identified by its UUID',
)
async def remove_task(uuid_: uuid.UUID, db: DBSession = Depends(get_db)):
    try:
        db.remove_task(uuid_)
    except KeyError as exception:
        raise HTTPException(
            status_code=404,
            detail='Task not found',
        ) from exception


@router.delete(
    '',
    summary='Deletes all tasks, use with caution',
    description='Deletes all tasks, use with caution',
)
async def remove_all_tasks(db: DBSession = Depends(get_db)):
    db.remove_all_tasks()
