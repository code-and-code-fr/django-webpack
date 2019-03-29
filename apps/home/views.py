"""Home views."""

from django.views.generic.base import TemplateView


class HomePageView(TemplateView):
    """Return the home page."""

    template_name = "home.html"

    def get_context_data(self, **kwargs):
        """Return the context."""
        context = super().get_context_data(**kwargs)
        context['title'] = "Home sweet home"
        return context
