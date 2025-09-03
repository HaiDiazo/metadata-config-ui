import reflex as rx

config = rx.Config(
    app_name="portal_management",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)