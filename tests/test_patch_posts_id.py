def test_put_post_id(create_test_date, create_post, patch_post, delete_post):
    test_date = create_post.post_posts(create_test_date)
    patch_post.patch_posts_id(create_test_date, test_date["id"])
    patch_post.check_response_status_is_ok()
    patch_post.check_response_body_same_as_change_body()
    patch_post.check_response_title_same_as_change_title()
    patch_post.check_response_post_id_same_as_change_post_id()
    patch_post.check_response_userid_same_as_change_userid()
    delete_post.delete_post(test_date["id"])