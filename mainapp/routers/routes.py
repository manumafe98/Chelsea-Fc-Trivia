from fastapi import APIRouter, Request, HTTPException, status
from fastapi.templating import Jinja2Templates


router = APIRouter()

@router.get("/")
async def trivia():
    pass


@router.post("/")
async def trivia_logic():
    pass



# TODO investigate how to make the loop, so it gives a total of 10 questions


# TODO create 3 arrays one to randomize if the question will be of player or attribute, 
# and the other with the respective questions

# TODO Pass to the template
# is player question? boolean, if true the options will be players attributes instead of player names, example goals
# attribute, pass it to the template so the template knows what player attribute to use in the options
# json element, the whole json to get the data from
