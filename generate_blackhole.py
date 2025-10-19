import sys

def generate_animated_blackhole_svg():
    svg_content = """
    <svg width="400" height="400" viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <filter id="glow">
          <feGaussianBlur in="SourceGraphic" stdDeviation="5" result="blur" />
          <feMerge>
            <feMergeNode in="blur" />
            <feMergeNode in="SourceGraphic" />
          </feMerge>
        </filter>
      </defs>

      <circle cx="200" cy="200" r="80" fill="#000000" filter="url(#glow)">
        <animate attributeName="r" from="78" to="82" dur="2s" repeatCount="indefinite" begin="0s;anim2.end" id="anim1"/>
        <animate attributeName="r" from="82" to="78" dur="2s" repeatCount="indefinite" begin="anim1.end" id="anim2"/>
      </circle>

      <circle cx="200" cy="200" r="150" fill="none" stroke="#FFD700" stroke-width="5" stroke-opacity="0.6">
        <animateTransform attributeName="transform"
                          attributeType="XML"
                          type="rotate"
                          from="0 200 200"
                          to="360 200 200"
                          dur="20s"
                          repeatCount="indefinite"/>
        <animate attributeName="stroke-opacity" from="0.6" to="0.3" dur="4s" repeatCount="indefinite" begin="0s;animop2.end" id="animop1"/>
        <animate attributeName="stroke-opacity" from="0.3" to="0.6" dur="4s" repeatCount="indefinite" begin="animop1.end" id="animop2"/>
      </circle>

      <circle cx="200" cy="200" r="120" fill="none" stroke="#FF8C00" stroke-width="3" stroke-opacity="0.8">
         <animateTransform attributeName="transform"
                          attributeType="XML"
                          type="rotate"
                          from="360 200 200"
                          to="0 200 200"
                          dur="15s"
                          repeatCount="indefinite"/>
        <animate attributeName="stroke-opacity" from="0.8" to="0.5" dur="3s" repeatCount="indefinite" begin="0s;animopi2.end" id="animopi1"/>
        <animate attributeName="stroke-opacity" from="0.5" to="0.8" dur="3s" repeatCount="indefinite" begin="animopi1.end" id="animopi2"/>
      </circle>

      <rect x="0" y="0" width="400" height="400" fill="url(#starfield)"/>
      <defs>
        <pattern id="starfield" x="0" y="0" width="10" height="10" patternUnits="userSpaceOnUse">
          <circle cx="1" cy="1" r="0.5" fill="white" opacity="0.1"/>
          <circle cx="8" cy="5" r="0.3" fill="white" opacity="0.05"/>
          <circle cx="3" cy="8" r="0.4" fill="white" opacity="0.07"/>
        </pattern>
      </defs>

    </svg>
    """
    return svg_content

if __name__ == "__main__":
    svg_output = generate_animated_blackhole_svg()
    # Write to stdout so GitHub Action can capture it or directly to a file
    # For GitHub Actions, writing to a file is often easier
    with open("blackhole_animation.svg", "w") as f:
        f.write(svg_output)