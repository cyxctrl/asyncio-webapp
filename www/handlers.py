from coroweb import get
from models import User


@get('/')
async def index():
    users = await User.find_all()
    return {
        '__template__': 'test.html',
        'users': users
    }
