




<!-- model -->
class Skills(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    cover_image = models.ImageField("skills/images/", blank=True, null=True)
    percentage = models.IntegerField(blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.name}"

<!-- admin -->
admin.site.register(Skills)

<!-- view -->
def skills_view(request):
    skills = Skills.objects.all()  # Fetch all skills
    print(skills)  # Debug: Print skills in the console
    return render(request, 'skil.html', {'skills': skills})

<!-- html -->
<!-- {% load static %}

<section id="skills" class="skill-area">
    <div class="container">
        <div class="row justify-content-center">
            <div class="col-xl-12 col-lg-12">
                <div class="section-title text-center mb-60 wow fadeInUp delay-0-2s">
                    <p>Pro Skills</p>
                    <h2>Let’s Explore My Skills</h2>
                </div>
            </div>
        </div>
        <div class="row">
            <div class="col-lg-12">
                <div class="skill-items-wrap">
                    <div class="row">
                        {% for skill in skills %}
                            <div class="col-lg-3 col-sm-6 col-xs-12">
                                <div class="skill-item wow fadeInUp delay-0-2s">
                                    {% if skill.cover_image %}
                                        <img src="{{ skill.cover_image.url }}" alt="{{ skill.name }}">
                                    {% else %}
                                        <img src="{% static 'assets/images/skills/skill1.png' %}" alt="No Image">
                                    {% endif %}
                                    <h5>{{ skill.name }}</h5>
                                    <span class="percent">{{ skill.percentage }}%</span>
                                </div>
                            </div>
                        {% empty %}
                            <p>No skills available.</p>
                        {% endfor %}
                    </div>
                </div>
            </div>
        </div>
    </div>
</section> -->


<!-- urls -->
path('skills/', V.skills_view, name='skills'),

