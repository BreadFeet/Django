from django.shortcuts import render

from db.dao.itemdb import ItemDB
from db.dao.userdb import UserDB
from db.frame.sqlitedao import SqliteDao
from db.vo.uservo import UserVO
from db.vo.itemvo import ItemVO           # itemlist.html 때문이 아니라 view.additem 위해서 import

sqlitedao = SqliteDao('shop.db')
sqlitedao.makeTable()
udb = UserDB('shop.db')
idb = ItemDB('shop.db')

# Create your views here.
def home(request):
    return render(request, 'base.html')


def login(request):
    context = {
        'section': 'login_teacher.html'
    }
    return render(request, 'base.html', context)


def loginimpl(request):    # request는 url 쿼리인가????????????????????????/
    id = request.POST['id']       # post로 보낸 name="id"와 "pwd"값을 받음
    pwd = request.POST['pwd']     # POST는 무조건 대문자! 소문자는 오류남!
    print(id, pwd)                # 확인차 터미널 출력

    ##### 실제 입력받은 값을 db와 연동하여 확인하는 방법 ################################################################
    # 나)) id를 넣어서 VO로 만들고 getId, getPwd...등을 해서 sql쿼리를 만들어서 DB가 데이터베이스에서 select해서 나오는지 확인??
    context = {}
    try:
        user_s = udb.select(id)       # 불러온 user_s는 UserVO 객체임!!
        print(user_s)
        if pwd == user_s.getPwd():    # id, pwd가 모두 맞는 경우
            # session에 사용자 정보를 넣는다
            request.session['sessionid'] = id
            # section에 loginok.html 화면을 넣는다
            context['section'] = 'loginok.html'
            context['logid'] = user_s       # 이후 출력페이지에서 id, pwd, name값 사용하기 위해서 VO객체로 받음
        else:                    # id는 존재하지만, pwd가 틀린 경우 오류 발생
            raise Exception("비번 오류********", "비번망했슈.......:/")
                  # error 이름은 IndexError, NameError 등 내장 에러 아무거나 가능!!
    except Exception as msg:                # id가 db에 없으면 sql 반환값 없음 -> UserVO에 넣을게 없어서 오류남!!
        # section에 loginfail.html 화면을 넣는다
        context['section'] = 'loginfail.html'
        print(msg.args[1])
        # Exception은 모든 오류상황을 말하는 것이라, id가 없는 경우에도 except가 실행된다!!!
        # -> 다만 설정된 msg가 없기 때문에 출력되는 내용은 없음

    return render(request, 'base.html', context)

    ###### db연결 없이 임의의 옳은 id, pwd값이 있다고 가정한 해결방식#####################################################
    # 1. 입력한 ID가 화원가입된 ID인지 검사
    # 2. 입력한 PWD가 회원가입 시 입력한 PWD와 동일한지 검사
    # context = {}                                  # 먼저 선언해줘야 함!
    # if id == 'qq' and pwd == '00':
    #     request.session['sessionid'] = id         # login이 정상적으로 일어났을 때, 서버의 session 사전에 id값 추가
    #     context['section'] = 'loginok.html'       # 사전 기능 활용!
    #     context['logid'] = 'qq'
    #     # centerpage = 'loginok.html'
    #     id = 'qq'
    #
    # else:
    #     context['section'] = 'loginfail.html'
    #     # centerpage = 'loginfail.html'
    #
    # 3. 로그인 정상 처리
    # 4. 로그인 실패 처리
    # context = {
    #     'section': centerpage,
    #     'lid': id,
    # }
    # return render(request, 'base.html', context)


def reg(request):
    context = {
        'section': 'reg_teacher.html'
    }
    return render(request, 'base.html', context)


def regimpl(request):
    id = request.GET['id']
    pwd = request.GET['pwd']
    name = request.GET['name']
    print(id, pwd, name)
    # 회원 정보를 데이터베이스에 저장한다
    user = UserVO(id, pwd, name)
    udb.insert(user)
    # 회원 가입 완료 메세지를 화면에 표시
    context = {
        'section':'registerok.html',
        'rname': (id, name),                # 위의 name값을 출력
    }
    return render(request, 'base.html', context)


def logout(request):
    if request.session['sessionid'] != None:    # 이 과정에서 오류나면 python manage.py migrate 실행
        del request.session['sessionid']        # del: 사전 지우는 법
    return render(request, 'base.html')


def html5(request):
    context = {
        'section': 'html5.html'        # section이라는 변수에는 html5.html파일을 넣으라는 지정
    }
    return render(request, 'base.html', context)

def css(request):
    context = {
        'section': 'css.html'
    }
    return render(request, 'base.html', context)

def js(request):
    context = {
        'section': 'js.html'
    }
    return render(request, 'base.html', context)

def jq(request):
    context = {
        'section': 'jq.html'
    }
    return render(request, 'base.html', context)

def ajax(request):
    context = {
        'section': 'ajax.html'
    }
    return render(request, 'base.html', context)


def userli(request):
    # selecAll로 모든 유저정보 가져온다
    allusers = udb.selectAll()
    for a in allusers:
        a
    # 가져온 정보를 section에 띄운다.
    context = {
        'section': 'userlist.html',
        'list': allusers,
        'l': a,
    }
    return render(request, 'base.html', context)


def userdtl(request):
    # 클릭한 id값을 추출
    id = request.GET['id']
    # 요청한 id 정보의 상세 정보를 조회 - select로 불러옴
    user = udb.select(id)
    # 상세 화면을 이동
    context = {
        'section': 'userdetail.html',
        'detail': user
    }
    return render(request, 'base.html', context)


def itemli(request):
    allitems = idb.selectAll()
    context = {
        'section': 'itemlist.html',
        'list': allitems,
    }
    return render(request, 'base.html', context)

def itemdtl(a):                  # 장고가 자동으로 함수의 첫번째 인자를 지정하므로 바꿔도 됨!!!!
    id = int(a.GET['id'])        # string -> int
    item = idb.select(id)
    context = {
        'section': 'itemdetail.html',
        'detail': item,
    }
    return render(a, 'base.html', context)


def additem(request):
    context = {
        'section': 'additem.html'
    }
    return render(request, 'base.html', context)


def addimpl(request):
    # name, price가 입력되면, VO 만들어서 insert
    name = request.GET['name']
    price = float(request.GET['price'])
    # print(type(price))                # string --> float
    item = ItemVO(0, name, price, '')
    idb.insert(item)
    context = {
        'section': 'additemok.html',
        # 'item_i': item,              # VO로 넣어서 additem.html에서 getter를 쓸 수도 있음
        'item_n': name,
        'item_p': price,
    }
    return render(request, 'base.html', context)