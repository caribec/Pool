            mouse_pos = pygame.mouse.get_pos()
            cue.rect.center = balls[-1].body.position
            x_dist = balls[-1].body.position[0] - mouse_pos[0]
            y_dist = -(balls[-1].body.position[1] - mouse_pos[1])
            cue_angle = math.degrees(math.atan2(y_dist, x_dist))
            cue.update(cue_angle)
            cue.draw(screen)