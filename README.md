진짜 기본적인 포스트 기능만 구혔했는데 (새 글 작성, 업데이트(글 쓴 시간 나타남))
기존 클래스 모델과 연동하는 것을 진짜 잘 모르겠어서 피드백 한번 부탁드립니다..(일단 주석처리 해놈)
추가적으로 기능과 템플릿에 대해서 좀 더 구현해보겠습니다

- *커밋에 대해서 comment 달아 놓았습니다. view랑 model 커밋 각각 올라가 있으니 확인하고 쉽게-절차적으로 순서를 생각하고 해결해보세요.*
- *기존 모델은 우리가 처음에 erd를 짜면서 합의한 것이니, 해당 erd를 생각하면서 작업하면 어디부터 해결해야하는지 무슨기능이 필요한지 떠오를 수 있습니다.*
- *erd-create-detail 이게 생성순서입니다. create가 힘들면 일단 admin 에서 만드는 것부터 시작해보세요 파이팅*

# py_pro

- ## tooltips
    - POSITIVE_INTEGER is 0~2147483647
    - delete db and reset? delet all migrations/*.py and *.pyc except __init__.py.
    - POSTIVE_INTEGER default null ? means not in a stock

- ## commands
    - ``./manage.py graph_models -a -g -o my_project_visualized.png``

- ## model_story_relation
    - AS:ANONUMOUS_USER
        1. visit index, see list of representational products,
            - ack: login and register button somewhere
            - ack: list of drinks is represtational not listing in detail.
            - dev_todo: show posts those likes aheads above them
            - user_todo
                - signin, signup
                - press single respresentational drink
                - press list-menu of drinks to filter or find something.
                - press post-menu to see how much these users are on active

        2. Press listpage of drinks
            - ack: default list is based on filter; a filter ``updated_at`` based.
            - ack: category_filter [default = all] select panel exists, ie) liqur, vodka, beer?
            - ack: ordering_filter [default = updated_at in descending] ie) price, likes, postscount, selling, updated_at
            - ack: keyword_seach_filter, [brand, product_name]
            - user_todo
                - find exact he likes to drink or for present to other,

- ## TODO
    - Cart > CartItem 으로 재설정함
        - payment가 Cart를 가질 필요는 없지만, CartItem을 유지해줘야함.
    
    -

- ## model_tips:
    - Cartitem은 장바구니에 있는 동안은, 원 가격을 바라봐야하고  
    결제로 넘어가고 나면 정수로 유지되는데, 만약 결재 전에 수정을 하는 사항이 발생한다면?
    - CartItem은 drink를 바라보기때문에 price필드는 마지막에 drink의 가격을 반영한 상태로 정수로 저장
 



