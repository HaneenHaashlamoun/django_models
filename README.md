# django_models

https://github.com/HaneenHaashlamoun/django_models/pull/1

## Feature Tasks and Requirements
## Model
- [x] create snack_tracker_project project
    - [x] This will involve some preliminary steps.
    - [x] Review previous class lab for details.
- [x] create snacks app
- [x] Add snacks app to project
- [x] create Snack model
    - [x] make sure it extends from proper base class
    - [x] add name as a CharField with maximum length of 64 characters.
    - [x] add purchaser ForeignKey related to Django’s built in user model with CASCADE delete option.
        from django.contrib.auth import get_user_model
    - [x] add description TextField

- [x] add model to admin
- [x] modify Snack model have user friendly display in admin
- [x] create migrations and migrate data
- [x] create a super user
- [x] run development server
- [x] Add a few snacks via Admin panel
- [x] create another user and more snacks via Admin panel
- [x] confirm that snacks behave as expected with proper name, purchaser and description.
- [x] Looks like your model in good shape. Congrats!

## Views for Snacks App
- [x] Where to create these views?
    - [x] Dig around and see if there’s a sensible spot.
    - [x] HINT There is one correct place for your app’s views.
- [x] create SnackListView
    - [x] extend ListView
    - [x] give a template of snack_list.html
    - [x] associate Snack model
- [x] update url patterns for project
    - [x] empty path should include snacks.urls
- [x] update snacks app urls
    - [x] empty sub-path should be handled by SnackListView
        - [x] Don’t forget to use as_view()
- [x] add detail view
    - [x] link snack_detail.html template
    - [x] associate Snack model
- [x] update app urlpatterns to handle detail view
    - [x] account for primary key in url
    - [x] path would look like localhost:8000/1/ to get to snack with id of 1

## Templates
- [x] Addtemplates folder in root of project
    - [x] register templates folder in project settings TEMPLATES section
- [x] create base.html ancestor template
    - [x] add main html document
    - [x] use Django Templating Language to allow child templates to insert - [x] content
- [x] create snack_list.html template
   - [x] extend base template
   - [x] use Django Templating Language to display each snack’s name
- [x] view home page (aka snack_list) and confirm snacks showing properly
- [x] create snack_detail.html template
    - [x] template should extend base
    - [x] content should display snack’s name, description and purchaser
- [x] add link in snack_list template to related detail page for each snack
- [x] Add a link back to Home (aka snack_list) page from detail page.

## User Acceptance Tests
- [x] Test Snack pages
    - [x] NOTE make sure test extends TestCase instead of SimpleTestCase used in previous class.
    - [x] verify status code
    - [x] verify correct template use
    - [x] use url name instead of hard coded path
        TIP: django.urls.reverse will help with that.