import colorsys

import flet
from flet import *
import flet.map as map


def main(page: Page):
    page.window.always_on_top = True
    page.window.width = 750

    def handle_tap(e: map.MapTapEvent):
        print(e)

    page.add(
        m := map.Map(
            expand=True,
            initial_center=map.MapLatitudeLongitude(59.98384061127106, 30.385641532738237),
            initial_zoom=13,
            on_init=lambda e: print('Map Init'),
            on_tap=handle_tap,
            layers=[map.TileLayer(url_template='https://tile.openstreetmap.org/{z}/{x}/{y}.png'),
                    map.CircleLayer(
                        circles=[
                            map.CircleMarker(
                                radius=10,
                                coordinates=map.MapLatitudeLongitude(50.5, 30.5),
                                color=Colors.BLUE,
                                border_color=Colors.RED,
                                border_stroke_width=5,
                            )
                        ]
                    ),
                    # map.PolygonLayer(
                    #     polygons=[
                    #         map.PolygonMarker(
                    #             label='Random Label',
                    #             label_text_style=TextStyle(
                    #                 color=Colors.WHITE,
                    #                 size=20
                    #             ),
                    #             color=Colors.BLUE_ACCENT_200,
                    #             coordinates=[map.MapLatitudeLongitude(58.4, 31.7),
                    #                          map.MapLatitudeLongitude(55.8, 34.89),
                    #                          map.MapLatitudeLongitude(54.2, 41.9)]
                    #         )
                    #     ]
                    # ),
                    # map.PolylineLayer(
                    #     polylines=[
                    #         map.PolylineMarker(
                    #             color=Colors.BLACK,
                    #             border_stroke_width=10,
                    #             coordinates=[
                    #                 map.MapLatitudeLongitude(10, 10),
                    #                 map.MapLatitudeLongitude(30, 15),
                    #                 map.MapLatitudeLongitude(23, 40),
                    #                 map.MapLatitudeLongitude(17, 30),
                    #             ]
                    #         )
                    #     ]
                    # ),
                    map.MarkerLayer(
                        markers=[
                            map.Marker(
                                content=Icon(Icons.HOME,
                                             color=Colors.LIGHT_BLUE,
                                             size=30),
                                coordinates=map.MapLatitudeLongitude(59.98384061127106, 30.385641532738237),
                            )
                        ]
                    ),
                    map.RichAttribution(
                        # show_flutter_map_attribution=False,
                        attributions=[
                            map.TextSourceAttribution(
                                text='Flet',
                                on_click=lambda e: page.launch_url('https://flet.dev'),
                            )
                        ]
                    ),
                    map.SimpleAttribution(
                        text='Simple Attribution',
                        alignment=alignment.top_center,
                    )
                    ]
        ),
        Row(
            [
                OutlinedButton(text='Rotate 90°',
                               on_click=lambda e: m.rotate_from(90, AnimationCurve.EASE_IN)),
                OutlinedButton(text='Rotate -90°',
                               on_click=lambda e: m.rotate_from(-90, AnimationCurve.EASE_OUT)),
                OutlinedButton(text='My Home',
                               on_click=lambda e: m.move_to(
                                   destination=map.MapLatitudeLongitude(59.98384061127106, 30.385641532738237),
                                   animation_curve=AnimationCurve.EASE_IN,
                                   animation_duration=Duration(
                                       seconds=2
                                   ),
                                   zoom=13
                               ),
                               ),
                OutlinedButton(text='Zoom in',
                               on_click=lambda e: m.zoom_in(AnimationCurve.EASE_IN,
                                                            animation_duration=Duration(seconds=2))),
                OutlinedButton(text='Zoom out',
                               on_click=lambda e: m.zoom_out(AnimationCurve.EASE_OUT,
                                                             animation_duration=Duration(seconds=2))
                               ),
                OutlinedButton(text='Zoom to',
                               on_click=lambda e: m.zoom_to(zoom=10,
                                                            animation_curve=AnimationCurve.EASE_OUT,
                                                            animation_duration=Duration(seconds=2))),
                OutlinedButton(text='Center on',
                               on_click=lambda e: m.center_on(point=map.MapLatitudeLongitude(40, 20),
                                                              zoom=15)),
            ],
            width=700,

        )

    )


if __name__ == '__main__':
    flet.app(target=main)  #view=AppView.WEB_BROWSER
