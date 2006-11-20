from zookeepr.tests.functional import *

class TestProfileController(ControllerTest):
    def test_profile_view(self):
        # set up
        p = model.Person(email_address='testguy@example.org',
                         handle='testguy',
                         fullname='Testguy McTest',
                         )
        objectstore.save(p)
        objectstore.flush()

        pid = p.id
        
        resp = self.app.get('/profile/%d' % p.id)

        resp.mustcontain("Testguy McTest")

        # clean up
        objectstore.delete(Query(model.Person).get(pid))
        objectstore.flush()


class TestSignedInProfileController(SignedInCRUDControllerTest):
    def test_profile_list(self):
        resp = self.app.get('/profile')

        resp = resp.follow()

        resp.mustcontain("Testguy McTest")
