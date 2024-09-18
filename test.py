from request import post_new_order , get_orders_track


#Анна Косарева, 21-я когорта — Диплом
def test_order_creation():
    creation_response = post_new_order()
    track_id = creation_response.json()['track']
    response = get_orders_track(track_id)
    assert response.status_code == 200

#pytest test.py
