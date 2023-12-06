from dependency_injector import containers, providers

from app.spotify.service import SpotifyService


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        packages=[
            "app",
        ]
    )

    config = providers.Configuration(ini_files=["config.ini"], strict=True)

    spotify_service = providers.Singleton(
        SpotifyService,
        client_id=config.spotify.client_id,
        client_secret=config.spotify.client_secret,
        redirect_uri=config.spotify.redirect_uri
    )
