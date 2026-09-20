import os
import sys
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

# -------------------------------------------------------------
# Color Palette Definitions (VTKRO Cyber Executive Theme)
# -------------------------------------------------------------
BG_COLOR = RGBColor(10, 15, 36)          # Dark Cyber Navy (#0A0F24)
CARD_BG = RGBColor(17, 25, 54)           # Rich Deep Slate Navy (#111936)
CARD_BORDER = RGBColor(30, 45, 92)       # Card Border (#1E2D5C)
CYAN_GLOW = RGBColor(0, 229, 255)        # Glowing Electric Cyan (#00E5FF)
CYAN_SOFT = RGBColor(56, 189, 248)       # Sky Blue (#38BDF8)
WHITE = RGBColor(255, 255, 255)          # Pure White (#FFFFFF)
TEXT_MUTED = RGBColor(156, 163, 175)     # Muted Slate (#9CA3AF)
TEXT_BODY = RGBColor(226, 232, 240)      # Clean Light Slate (#E2E8F0)
GOLD = RGBColor(251, 191, 36)            # Golden Warning / Accent (#FBBF24)
QUOTE_BOX_BG = RGBColor(13, 24, 48)      # Quote Box Background (#0D1830)
QUOTE_BORDER = RGBColor(0, 229, 255)     # Cyan Accent Line (#00E5FF)
GREEN_ACCENT = RGBColor(52, 211, 153)    # Emerald (#34D399)
RED_ACCENT = RGBColor(248, 113, 113)     # Coral / Red Alert (#F87171)
DARK_BAR = RGBColor(22, 33, 68)          # Bar / Pill fill

IMAGES_DIR = os.path.abspath("./bigli_images")

def create_presentation():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # Helper: Set background color of slide
    def set_slide_background(slide):
        bg = slide.shapes.add_shape(
            MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(7.5)
        )
        bg.fill.solid()
        bg.fill.fore_color.rgb = BG_COLOR
        bg.line.fill.background()
        return bg

    # Helper: Add standard slide header
    def add_header(slide, category, title, subtitle):
        # Category Tag
        cat_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.7), Inches(0.35))
        tf_cat = cat_box.text_frame
        tf_cat.word_wrap = True
        tf_cat.margin_left = tf_cat.margin_right = tf_cat.margin_top = tf_cat.margin_bottom = 0
        p_cat = tf_cat.paragraphs[0]
        p_cat.text = category.upper()
        p_cat.font.size = Pt(10)
        p_cat.font.bold = True
        p_cat.font.color.rgb = CYAN_GLOW
        p_cat.font.name = "Segoe UI"

        # Main Title
        title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.72), Inches(11.7), Inches(0.55))
        tf_title = title_box.text_frame
        tf_title.word_wrap = True
        tf_title.margin_left = tf_title.margin_right = tf_title.margin_top = tf_title.margin_bottom = 0
        p_title = tf_title.paragraphs[0]
        p_title.text = title
        p_title.font.size = Pt(22)
        p_title.font.bold = True
        p_title.font.color.rgb = WHITE
        p_title.font.name = "Segoe UI"

        # Subtitle
        sub_box = slide.shapes.add_textbox(Inches(0.8), Inches(1.25), Inches(11.7), Inches(0.35))
        tf_sub = sub_box.text_frame
        tf_sub.word_wrap = True
        tf_sub.margin_left = tf_sub.margin_right = tf_sub.margin_top = tf_sub.margin_bottom = 0
        p_sub = tf_sub.paragraphs[0]
        p_sub.text = subtitle
        p_sub.font.size = Pt(12)
        p_sub.font.color.rgb = TEXT_MUTED
        p_sub.font.name = "Segoe UI"

    # -------------------------------------------------------------
    # SLIDE 1: Title Slide (Welcome Masterclass)
    # -------------------------------------------------------------
    slide1 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide1)

    # Top Cyan Accent Line
    line1 = slide1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(0.6), Inches(2.5), Inches(0.06))
    line1.fill.solid()
    line1.fill.fore_color.rgb = CYAN_GLOW
    line1.line.fill.background()

    # Title Card Text Frame
    t_box = slide1.shapes.add_textbox(Inches(0.8), Inches(0.85), Inches(6.8), Inches(5.8))
    tf1 = t_box.text_frame
    tf1.word_wrap = True
    tf1.margin_left = tf1.margin_right = tf1.margin_top = tf1.margin_bottom = 0

    p = tf1.paragraphs[0]
    p.text = "VTKRO CONSULTING ACADEMY"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = CYAN_GLOW

    p2 = tf1.add_paragraph()
    p2.text = "Agent Sales\nMasterclass"
    p2.font.size = Pt(38)
    p2.font.bold = True
    p2.font.color.rgb = WHITE
    p2.space_before = Pt(8)
    p2.space_after = Pt(12)

    p3 = tf1.add_paragraph()
    p3.text = "How to Consult Clients, Pitch Solutions & Close Deals Like a Pro"
    p3.font.size = Pt(16)
    p3.font.color.rgb = CYAN_SOFT
    p3.space_after = Pt(16)

    p4 = tf1.add_paragraph()
    p4.text = (
        "Congratulations on starting your high-earning journey with VTKRO! "
        "This masterclass contains field-tested consulting frameworks created from real-world success. "
        "Learn how to target clients, master cold and warm introductions, present our high-ROI packages, "
        "defend your pricing, and book high-converting senior strategist demos."
    )
    p4.font.size = Pt(12)
    p4.font.color.rgb = TEXT_BODY
    p4.space_after = Pt(20)

    # Trainer Badge Box
    p5 = tf1.add_paragraph()
    p5.text = "Lead Consultant & Author: SANJAI KUMAR | VTKRO Digital Solutions"
    p5.font.size = Pt(12)
    p5.font.bold = True
    p5.font.color.rgb = GOLD

    # Image Card Container (Right Side)
    img_card = slide1.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE, Inches(8.0), Inches(0.85), Inches(4.5), Inches(5.8)
    )
    img_card.fill.solid()
    img_card.fill.fore_color.rgb = CARD_BG
    img_card.line.color.rgb = CARD_BORDER
    img_card.line.width = Pt(1.5)

    # Insert Bigli Welcome Image
    img_welcome_path = os.path.join(IMAGES_DIR, "bigli_welcome_1789839363772.jpg")
    if os.path.exists(img_welcome_path):
        slide1.shapes.add_picture(img_welcome_path, Inches(8.25), Inches(1.05), Inches(4.0), Inches(4.0))

    # Caption beneath image
    cap_box = slide1.shapes.add_textbox(Inches(8.2), Inches(5.2), Inches(4.1), Inches(1.2))
    tf_cap = cap_box.text_frame
    tf_cap.word_wrap = True
    p_cap = tf_cap.paragraphs[0]
    p_cap.text = "Meet Bigli! Your VTKRO Sales Guide"
    p_cap.font.size = Pt(13)
    p_cap.font.bold = True
    p_cap.font.color.rgb = CYAN_GLOW
    p_cap.alignment = PP_ALIGN.CENTER

    p_cap2 = tf_cap.add_paragraph()
    p_cap2.text = "Follow Bigli's visual blueprints across every slide to master client interactions and maximize your commissions."
    p_cap2.font.size = Pt(10)
    p_cap2.font.color.rgb = TEXT_MUTED
    p_cap2.alignment = PP_ALIGN.CENTER

    slide1.notes_slide.notes_text_frame.text = (
        "TRAINER NOTES - WELCOME & INTRODUCTION:\n"
        "Welcome your new agents with high energy! Set the tone that selling VTKRO services is consultative and prestigious. "
        "Remind agents that this training is built from real, hands-on closing experience by Agent Consultant Sanjai Kumar. "
        "Bigli represents the ideal agent attitude: cheerful, persistent, structured, and strictly adhering to the system."
    )

    # -------------------------------------------------------------
    # SLIDE 2: Targeting Strategy (Big vs Small Businesses)
    # -------------------------------------------------------------
    slide2 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide2)
    add_header(
        slide2,
        "// Module 01: Client Intelligence",
        "Targeting Strategy: Big Businesses vs. Small Businesses",
        "Different business sizes have completely opposite buying psychology. Match your pitch to their true motivation."
    )

    # Left Card
    card_left = slide2.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.7), Inches(7.0), Inches(5.2)
    )
    card_left.fill.solid()
    card_left.fill.fore_color.rgb = CARD_BG
    card_left.line.color.rgb = CARD_BORDER

    tf2 = card_left.text_frame
    tf2.word_wrap = True
    tf2.margin_left = Inches(0.3)
    tf2.margin_right = Inches(0.3)
    tf2.margin_top = Inches(0.3)

    p = tf2.paragraphs[0]
    p.text = "1. Big Businesses (Hospitals, Malls, Luxury Cafes, Supermarkets)"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = CYAN_GLOW

    p = tf2.add_paragraph()
    p.text = (
        "• Core Value: QUALITY & AUTHORITY over price.\n"
        "• Buyer Psychology: Large business owners fear bad aesthetics, downtime, and unprofessional tech. "
        "They do not care about saving ₹5,000—they care about brand prestige and scaling.\n"
        "• Tactical Strategy: Offer multiple bundled services (Custom Multi-page Site, WhatsApp AI automation, "
        "Secure Payment Gateway, and Digital NFC staff cards). Position VTKRO as a comprehensive digital transformation partner."
    )
    p.font.size = Pt(11)
    p.font.color.rgb = TEXT_BODY
    p.space_after = Pt(12)

    p = tf2.add_paragraph()
    p.text = "2. Small Businesses (Local Bakeries, Salons, Garages, Neighborhood Clinics)"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = GREEN_ACCENT

    p = tf2.add_paragraph()
    p.text = (
        "• Core Value: COST-EFFICIENCY & IMMEDIATE ROI.\n"
        "• Buyer Psychology: Small merchants are budget-conscious and worried about expensive monthly agency retainers. "
        "They want proof that customers will walk through the door or call their phone.\n"
        "• Tactical Strategy: Pitch our transparent, cost-efficient packages. Emphasize zero hidden charges, "
        "instant WhatsApp inquiry buttons, and lightning-fast local customer capture."
    )
    p.font.size = Pt(11)
    p.font.color.rgb = TEXT_BODY
    p.space_after = Pt(12)

    p = tf2.add_paragraph()
    p.text = "GOLDEN CONSULTANT RULE:"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = GOLD

    p = tf2.add_paragraph()
    p.text = "Never pitch 'cheap & budget' to a hospital director, and never overwhelm a local bakery owner with complex corporate enterprise jargon!"
    p.font.size = Pt(11)
    p.font.color.rgb = WHITE

    # Right Bigli Image Card
    card_right = slide2.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE, Inches(8.1), Inches(1.7), Inches(4.4), Inches(5.2)
    )
    card_right.fill.solid()
    card_right.fill.fore_color.rgb = CARD_BG
    card_right.line.color.rgb = CARD_BORDER

    img_biz = os.path.join(IMAGES_DIR, "bigli_biz_types_1789839390139.jpg")
    if os.path.exists(img_biz):
        slide2.shapes.add_picture(img_biz, Inches(8.3), Inches(1.9), Inches(4.0), Inches(4.0))

    cap_box = slide2.shapes.add_textbox(Inches(8.2), Inches(6.0), Inches(4.2), Inches(0.8))
    tf = cap_box.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "Bigli's Balancing Act: Quality for Enterprise, Cost-Efficiency for Local Retail"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = CYAN_GLOW
    p.alignment = PP_ALIGN.CENTER

    slide2.notes_slide.notes_text_frame.text = (
        "TRAINER NOTES - TARGETING STRATEGY:\n"
        "Explain that the fastest way to lose a hospital or mall is to say 'we are cheap'. They will assume our work is shoddy. "
        "Conversely, if you pitch a ₹50,000 multi-system stack to a corner chai cafe, they will get scared and ghost you. "
        "Teach agents to categorize every lead in their notebook as 'Quality Focus' or 'Cost-Efficiency Focus' before dialing."
    )

    # -------------------------------------------------------------
    # SLIDE 3: How to Approach a Client (Call First Rule)
    # -------------------------------------------------------------
    slide3 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide3)
    add_header(
        slide3,
        "// Module 02: Initial Outreach Protocol",
        "The Initial Approach: Why You Must ALWAYS Call First",
        "The difference between a scheduled high-ticket consultation and an instant rejection at the front door."
    )

    card_left = slide3.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.7), Inches(7.0), Inches(5.2)
    )
    card_left.fill.solid()
    card_left.fill.fore_color.rgb = CARD_BG
    card_left.line.color.rgb = CARD_BORDER

    tf = card_left.text_frame
    tf.word_wrap = True
    tf.margin_left = Inches(0.3)
    tf.margin_right = Inches(0.3)
    tf.margin_top = Inches(0.3)

    p = tf.paragraphs[0]
    p.text = "1. The Mandatory Phone Briefing (DO THIS ALWAYS)"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = CYAN_GLOW

    p = tf.add_paragraph()
    p.text = (
        "• High Respect for Time: Calling first respects the business owner's schedule.\n"
        "• Qualify & Hook: A 2-minute phone briefing establishes your professional identity as a VTKRO consultant.\n"
        "• Confirmed Calendar: It allows you to lock in a dedicated meeting time (in-person or virtual demo) "
        "where the owner is mentally prepared to listen to business solutions."
    )
    p.font.size = Pt(11)
    p.font.color.rgb = TEXT_BODY
    p.space_after = Pt(14)

    p = tf.add_paragraph()
    p.text = "2. CRITICAL AVOID: Never Walk in Unannounced!"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = RED_ACCENT

    p = tf.add_paragraph()
    p.text = (
        "• Instant Defensive Rejection: If you barge in unexpectedly, the owner is likely busy dealing with "
        "customers, billing, or staff issues. You will be seen as an interruption and rejected immediately.\n"
        "• Lowered Status: Unannounced walk-ins make you look like a desperate salesperson rather than a high-value technical consultant."
    )
    p.font.size = Pt(11)
    p.font.color.rgb = TEXT_BODY
    p.space_after = Pt(14)

    p = tf.add_paragraph()
    p.text = "THE NEIGHBORHOOD RESIDENCY RULE:"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = GOLD

    p = tf.add_paragraph()
    p.text = "Even if the business is right next to your home or across your street, CALL FIRST. Familiarity does not replace professional protocol."
    p.font.size = Pt(11)
    p.font.color.rgb = WHITE

    # Right Bigli Image Card
    card_right = slide3.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE, Inches(8.1), Inches(1.7), Inches(4.4), Inches(5.2)
    )
    card_right.fill.solid()
    card_right.fill.fore_color.rgb = CARD_BG
    card_right.line.color.rgb = CARD_BORDER

    img_phone = os.path.join(IMAGES_DIR, "bigli_phone_call_1789839412105.jpg")
    if os.path.exists(img_phone):
        slide3.shapes.add_picture(img_phone, Inches(8.3), Inches(1.9), Inches(4.0), Inches(4.0))

    cap_box = slide3.shapes.add_textbox(Inches(8.2), Inches(6.0), Inches(4.2), Inches(0.8))
    tf = cap_box.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "Bigli's Rule: Lock in a confirmed appointment on the phone. Never walk in blind!"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = CYAN_GLOW
    p.alignment = PP_ALIGN.CENTER

    slide3.notes_slide.notes_text_frame.text = (
        "TRAINER NOTES - HOW TO APPROACH:\n"
        "Emphasize this heavily: Amateurs walk into stores and ask 'Where is the owner?'. They get rejected 9 times out of 10. "
        "Professionals call the front desk or business line, ask for the decision maker, deliver the 120-second hook, "
        "and schedule a formal meeting slot. Once scheduled, when you walk in, they have a chair waiting for you."
    )

    # -------------------------------------------------------------
    # SLIDE 4: The Relative & Friend Trap (Defeating Discount Pressure)
    # -------------------------------------------------------------
    slide4 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide4)
    add_header(
        slide4,
        "// Module 03: Social Circle Consulting",
        "Approaching Relatives & Friends: Defeating the Discount Trap",
        "How to turn social pressure into strong career support while protecting your standard rates."
    )

    card_left = slide4.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.7), Inches(7.0), Inches(5.2)
    )
    card_left.fill.solid()
    card_left.fill.fore_color.rgb = CARD_BG
    card_left.line.color.rgb = CARD_BORDER

    tf = card_left.text_frame
    tf.word_wrap = True
    tf.margin_left = Inches(0.3)
    tf.margin_right = Inches(0.3)
    tf.margin_top = Inches(0.25)

    p = tf.paragraphs[0]
    p.text = "The Situation: When the Client is a Relative, Friend, or Acquaintance"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = CYAN_GLOW

    p = tf.add_paragraph()
    p.text = (
        "• You DO NOT need to cold call them—you can meet them directly because personal rapport already exists.\n"
        "• THE DANGER: They will almost certainly expect a heavy discount or want services for free ('Aren't you my nephew/friend?')."
    )
    p.font.size = Pt(10.5)
    p.font.color.rgb = TEXT_BODY
    p.space_after = Pt(8)

    # Script Box 1
    p = tf.add_paragraph()
    p.text = "SCRIPT OPTION 1: The Corporate Shield (Default)"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = GOLD

    p = tf.add_paragraph()
    p.text = (
        '"I am an authorized consultant for VTKRO. Our enterprise pricing, cloud hosting, and payment architecture '
        'are fixed strictly by higher corporate authorities. I am not permitted to modify official packages, '
        'but I will personally supervise your setup so you get VIP 24/7 onboarding."'
    )
    p.font.size = Pt(10)
    p.font.italic = True
    p.font.color.rgb = WHITE
    p.space_after = Pt(8)

    # Script Box 2
    p = tf.add_paragraph()
    p.text = "SCRIPT OPTION 2: The Intern Communication Challenge (If Insecure)"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = GREEN_ACCENT

    p = tf.add_paragraph()
    p.text = (
        '"I am currently working as a digital consultant intern at VTKRO. To pass my communication & business evaluation round, '
        'earn my professional certification and unlock my stipend, I am required to complete a verified sale at standard company rates. '
        'By setting up your website through me, you help me clear my official evaluation!"'
    )
    p.font.size = Pt(10)
    p.font.italic = True
    p.font.color.rgb = WHITE
    p.space_after = Pt(8)

    p = tf.add_paragraph()
    p.text = "Psychological Impact: Converts bargain pressure into genuine willingness to support your professional milestone."
    p.font.size = Pt(9.5)
    p.font.color.rgb = CYAN_SOFT

    # Right Bigli Image Card
    card_right = slide4.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE, Inches(8.1), Inches(1.7), Inches(4.4), Inches(5.2)
    )
    card_right.fill.solid()
    card_right.fill.fore_color.rgb = CARD_BG
    card_right.line.color.rgb = CARD_BORDER

    img_rel = os.path.join(IMAGES_DIR, "bigli_relatives_1789839555347.jpg")
    if os.path.exists(img_rel):
        slide4.shapes.add_picture(img_rel, Inches(8.3), Inches(1.9), Inches(4.0), Inches(4.0))

    cap_box = slide4.shapes.add_textbox(Inches(8.2), Inches(6.0), Inches(4.2), Inches(0.8))
    tf = cap_box.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "Bigli's Corporate Policy Shield: Protects your price and secures your hard-earned commission."
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = CYAN_GLOW
    p.alignment = PP_ALIGN.CENTER

    slide4.notes_slide.notes_text_frame.text = (
        "TRAINER NOTES - FRIENDS & RELATIVES:\n"
        "Many young agents fail because their uncles or friends talk them into giving away their commission. "
        "Teach them never to negotiate against themselves. Using the 'Corporate Authority' shield or 'Intern Evaluation Challenge' "
        "preserves the agent's professional standing and makes the client feel proud to help their career."
    )

    # -------------------------------------------------------------
    # SLIDE 5: Cold Call Opening (The 2-Minute Hook)
    # -------------------------------------------------------------
    slide5 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide5)
    add_header(
        slide5,
        "// Module 04: Telecalling Mastery",
        "Cold Call Opening: The 2-Minute Hook (Script & Voice Delivery)",
        "How to command immediate authority, build rapport, and win permission to speak in under 120 seconds."
    )

    card_left = slide5.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.7), Inches(7.0), Inches(5.2)
    )
    card_left.fill.solid()
    card_left.fill.fore_color.rgb = CARD_BG
    card_left.line.color.rgb = CARD_BORDER

    tf = card_left.text_frame
    tf.word_wrap = True
    tf.margin_left = Inches(0.3)
    tf.margin_right = Inches(0.3)
    tf.margin_top = Inches(0.25)

    p = tf.paragraphs[0]
    p.text = "THE OFFICIAL COLD CALL OPENING SCRIPT"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = CYAN_GLOW

    # Script Quote Box Inside
    q_box = slide5.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.05), Inches(2.15), Inches(6.5), Inches(2.55)
    )
    q_box.fill.solid()
    q_box.fill.fore_color.rgb = QUOTE_BOX_BG
    q_box.line.color.rgb = QUOTE_BORDER
    q_box.line.width = Pt(1)

    tf_q = q_box.text_frame
    tf_q.word_wrap = True
    tf_q.margin_left = Inches(0.2)
    tf_q.margin_right = Inches(0.2)
    tf_q.margin_top = Inches(0.15)

    p = tf_q.paragraphs[0]
    p.text = (
        '"Hello [Client\'s Name], good morning/afternoon!\n'
        'My name is [Agent Name] calling on behalf of VTKRO, a premier web development and digital solutions company.\n\n'
        'I\'m reaching out because we help businesses like [Client\'s Business Name] elevate their online presence, '
        'attract more customers, and automate their daily operations. We are currently offering specialized business growth website packages '
        'tailored to your exact industry needs.\n\n'
        'Do you have two minutes to discuss how a modern website could help scale your revenue?"'
    )
    p.font.size = Pt(10)
    p.font.italic = True
    p.font.color.rgb = WHITE

    # 3 Keys below script
    p = tf.add_paragraph()
    p.text = "\nTHREE SECRETS TO 100% SCRIPT DELIVERY:"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = GOLD

    p = tf.add_paragraph()
    p.text = (
        "1. Voice Modulation & Smile: Smile while speaking—warmth and confidence are instantly felt over the phone.\n"
        "2. Personalization: Never say 'your company'; say '[Business Name]' so they know you researched them.\n"
        "3. The 2-Minute Micro-Agreement: Asking for just 2 minutes reduces resistance and earns immediate listening time."
    )
    p.font.size = Pt(10)
    p.font.color.rgb = TEXT_BODY

    # Right Bigli Image Card
    card_right = slide5.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE, Inches(8.1), Inches(1.7), Inches(4.4), Inches(5.2)
    )
    card_right.fill.solid()
    card_right.fill.fore_color.rgb = CARD_BG
    card_right.line.color.rgb = CARD_BORDER

    img_cold = os.path.join(IMAGES_DIR, "bigli_cold_call_1789839581186.jpg")
    if os.path.exists(img_cold):
        slide5.shapes.add_picture(img_cold, Inches(8.3), Inches(1.9), Inches(4.0), Inches(4.0))

    cap_box = slide5.shapes.add_textbox(Inches(8.2), Inches(6.0), Inches(4.2), Inches(0.8))
    tf = cap_box.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "Bigli's 2-Minute Hook: High energy, clear articulation, and zero hesitation."
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = CYAN_GLOW
    p.alignment = PP_ALIGN.CENTER

    slide5.notes_slide.notes_text_frame.text = (
        "TRAINER NOTES - COLD CALL SCRIPT:\n"
        "Have the agents practice this aloud in pairs. The most common mistake is talking too fast. "
        "Tell them: Breathe, pronounce every syllable clearly, and pause after asking: 'Do you have two minutes to discuss how a modern website could scale your revenue?'. "
        "Wait for their response. When they say 'yes', smoothly proceed to the package breakdown."
    )

    # -------------------------------------------------------------
    # SLIDE 6: Warm Lead & Follow-Up Opening
    # -------------------------------------------------------------
    slide6 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide6)
    add_header(
        slide6,
        "// Module 05: Inbound & Follow-Up",
        "Warm Lead & Follow-Up Opening: Converting Curiosity into Sales",
        "How to contact leads who inquired via WhatsApp, social media ads, or referral partner links."
    )

    card_left = slide6.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.7), Inches(7.0), Inches(5.2)
    )
    card_left.fill.solid()
    card_left.fill.fore_color.rgb = CARD_BG
    card_left.line.color.rgb = CARD_BORDER

    tf = card_left.text_frame
    tf.word_wrap = True
    tf.margin_left = Inches(0.3)
    tf.margin_right = Inches(0.3)
    tf.margin_top = Inches(0.25)

    p = tf.paragraphs[0]
    p.text = "THE OFFICIAL WARM LEAD OPENING SCRIPT"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = CYAN_GLOW

    # Script Box
    q_box = slide6.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.05), Inches(2.15), Inches(6.5), Inches(2.4)
    )
    q_box.fill.solid()
    q_box.fill.fore_color.rgb = QUOTE_BOX_BG
    q_box.line.color.rgb = QUOTE_BORDER
    q_box.line.width = Pt(1)

    tf_q = q_box.text_frame
    tf_q.word_wrap = True
    tf_q.margin_left = Inches(0.2)
    tf_q.margin_right = Inches(0.2)
    tf_q.margin_top = Inches(0.15)

    p = tf_q.paragraphs[0]
    p.text = (
        '"Hi [Client\'s Name], this is [Agent Name] from VTKRO. Following up on your inquiry regarding digital solutions for [Client\'s Company Name].\n\n'
        'At VTKRO, we build custom, high-converting websites equipped with modern automation tools to help you stand out from competitors '
        'and convert website traffic into paying clients.\n\n'
        'I\'d love to walk you through three specialized packages we\'ve designed to fit different business scales."'
    )
    p.font.size = Pt(10.5)
    p.font.italic = True
    p.font.color.rgb = WHITE

    # Bridge below script
    p = tf.add_paragraph()
    p.text = "\nTHE SEAMLESS BRIDGE TO PACKAGES:"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = GOLD

    p = tf.add_paragraph()
    p.text = (
        '"Depending on where your business is currently focused, we have three tailored packages designed to give you the highest Return on Investment (ROI)..."\n\n'
        '• Speed to Lead: Call warm leads within 15 minutes of inquiry while their interest is peaked.\n'
        '• Reference Their Source: Mention whether they messaged on WhatsApp or filled out an online form.'
    )
    p.font.size = Pt(10)
    p.font.color.rgb = TEXT_BODY

    # Right Bigli Image Card
    card_right = slide6.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE, Inches(8.1), Inches(1.7), Inches(4.4), Inches(5.2)
    )
    card_right.fill.solid()
    card_right.fill.fore_color.rgb = CARD_BG
    card_right.line.color.rgb = CARD_BORDER

    img_warm = os.path.join(IMAGES_DIR, "bigli_warm_lead_1789839603684.jpg")
    if os.path.exists(img_warm):
        slide6.shapes.add_picture(img_warm, Inches(8.3), Inches(1.9), Inches(4.0), Inches(4.0))

    cap_box = slide6.shapes.add_textbox(Inches(8.2), Inches(6.0), Inches(4.2), Inches(0.8))
    tf = cap_box.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "Bigli's Inbound Rule: Check their inquiry details and smoothly transition into tailored solutions."
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = CYAN_GLOW
    p.alignment = PP_ALIGN.CENTER

    slide6.notes_slide.notes_text_frame.text = (
        "TRAINER NOTES - WARM INBOUND LEADS:\n"
        "Warm leads are 5x easier to close than cold leads, BUT only if called immediately. "
        "Studies show contacting a lead within 15 minutes increases closing likelihood by 400%. "
        "Remind agents: Don't beat around the bush; acknowledge their inquiry and immediately bridge into the 3 packages."
    )

    # -------------------------------------------------------------
    # SLIDE 7: Package 1 (Standard Starter Web Presence)
    # -------------------------------------------------------------
    slide7 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide7)
    add_header(
        slide7,
        "// Module 06: Product Portfolio (Tier 1)",
        "Package 1: Standard Starter Web Presence (₹15,000)",
        "The essential high-speed corporate anchor for businesses wanting instant credibility and local discovery."
    )

    card_left = slide7.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.7), Inches(7.0), Inches(5.2)
    )
    card_left.fill.solid()
    card_left.fill.fore_color.rgb = CARD_BG
    card_left.line.color.rgb = CARD_BORDER

    tf = card_left.text_frame
    tf.word_wrap = True
    tf.margin_left = Inches(0.3)
    tf.margin_right = Inches(0.3)
    tf.margin_top = Inches(0.25)

    p = tf.paragraphs[0]
    p.text = "OFFICIAL PRICE: ₹15,000 (One-Time Setup)"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = GREEN_ACCENT

    p = tf.add_paragraph()
    p.text = "Ideal For: Emerging clinics, local shops, accountants, gyms, and service contractors."
    p.font.size = Pt(10)
    p.font.color.rgb = TEXT_MUTED
    p.space_after = Pt(8)

    # Script Box
    q_box = slide7.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.05), Inches(2.45), Inches(6.5), Inches(1.8)
    )
    q_box.fill.solid()
    q_box.fill.fore_color.rgb = QUOTE_BOX_BG
    q_box.line.color.rgb = QUOTE_BORDER
    q_box.line.width = Pt(1)

    tf_q = q_box.text_frame
    tf_q.word_wrap = True
    tf_q.margin_left = Inches(0.2)
    tf_q.margin_right = Inches(0.2)
    tf_q.margin_top = Inches(0.12)

    p = tf_q.paragraphs[0]
    p.text = (
        '"If you need a sleek, high-performing corporate presence to establish trust, our Standard 3–5 Page Business Website is ideal. '
        'We design a mobile-responsive, lightning-fast website featuring your core services, about section, gallery, and contact conversion forms. '
        'It\'s perfect for establishing instant credibility when customers search for you online."'
    )
    p.font.size = Pt(10)
    p.font.italic = True
    p.font.color.rgb = WHITE

    # Features
    p = tf.add_paragraph()
    p.text = "\nWHAT'S INCLUDED IN THE ARCHITECTURE:"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = CYAN_GLOW

    p = tf.add_paragraph()
    p.text = (
        "• 3–5 Custom Responsive Web Pages (Home, About, Services, Gallery, Contact).\n"
        "• Mobile-First, Lightning Fast: Loads in under 1.5 seconds on all budget smartphones.\n"
        "• Contact Form & Google Maps: Lead capture sent straight to their email & WhatsApp.\n"
        "• Instant Local SEO: Ready for Google Search & business profile ranking."
    )
    p.font.size = Pt(10)
    p.font.color.rgb = TEXT_BODY

    # Right Bigli Image Card
    card_right = slide7.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE, Inches(8.1), Inches(1.7), Inches(4.4), Inches(5.2)
    )
    card_right.fill.solid()
    card_right.fill.fore_color.rgb = CARD_BG
    card_right.line.color.rgb = CARD_BORDER

    img_starter = os.path.join(IMAGES_DIR, "bigli_starter_1789839630050.jpg")
    if os.path.exists(img_starter):
        slide7.shapes.add_picture(img_starter, Inches(8.3), Inches(1.9), Inches(4.0), Inches(4.0))

    cap_box = slide7.shapes.add_textbox(Inches(8.2), Inches(6.0), Inches(4.2), Inches(0.8))
    tf = cap_box.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "Bigli's Starter Setup: Clean, rapid-loading website that builds instant credibility online."
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = CYAN_GLOW
    p.alignment = PP_ALIGN.CENTER

    slide7.notes_slide.notes_text_frame.text = (
        "TRAINER NOTES - PACKAGE 1:\n"
        "This is your high-volume door opener. If a client is hesitant about technology or spending a lot, "
        "position the ₹15,000 package as the essential digital hygiene requirement. "
        "Remind them: In 2026, a business without a fast website is invisible to 80% of modern buyers."
    )

    # -------------------------------------------------------------
    # SLIDE 8: Package 2 (Professional Branding & Payment Suite)
    # -------------------------------------------------------------
    slide8 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide8)
    add_header(
        slide8,
        "// Module 07: Product Portfolio (Tier 2)",
        "Package 2: Professional Branding & Payment Suite (₹25,000)",
        "The ultimate hybrid brand kit: accept online customer payments and share contacts with one NFC tap."
    )

    card_left = slide8.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.7), Inches(7.0), Inches(5.2)
    )
    card_left.fill.solid()
    card_left.fill.fore_color.rgb = CARD_BG
    card_left.line.color.rgb = CARD_BORDER

    tf = card_left.text_frame
    tf.word_wrap = True
    tf.margin_left = Inches(0.3)
    tf.margin_right = Inches(0.3)
    tf.margin_top = Inches(0.25)

    p = tf.paragraphs[0]
    p.text = "OFFICIAL PRICE: ₹25,000 (Complete Suite)"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = GREEN_ACCENT

    p = tf.add_paragraph()
    p.text = "Ideal For: Retail showrooms, doctors, salons, consultants, architects, and boutique stores."
    p.font.size = Pt(10)
    p.font.color.rgb = TEXT_MUTED
    p.space_after = Pt(8)

    # Script Box
    q_box = slide8.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.05), Inches(2.45), Inches(6.5), Inches(1.8)
    )
    q_box.fill.solid()
    q_box.fill.fore_color.rgb = QUOTE_BOX_BG
    q_box.line.color.rgb = QUOTE_BORDER
    q_box.line.width = Pt(1)

    tf_q = q_box.text_frame
    tf_q.word_wrap = True
    tf_q.margin_left = Inches(0.2)
    tf_q.margin_right = Inches(0.2)
    tf_q.margin_top = Inches(0.12)

    p = tf_q.paragraphs[0]
    p.text = (
        '"If you want to accept payments directly and build a modern brand presence, our Professional Package is the complete kit. '
        'You get a customized multi-page website integrated with a secure Payment Gateway. '
        'On top of that, we include Physical Professional Business Cards along with an interactive Digital Business Card '
        'so you can share your business profile with clients in a single tap via smartphone."'
    )
    p.font.size = Pt(10)
    p.font.italic = True
    p.font.color.rgb = WHITE

    # Features
    p = tf.add_paragraph()
    p.text = "\nWHAT'S INCLUDED IN THE HYBRID BUNDLE:"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = CYAN_GLOW

    p = tf.add_paragraph()
    p.text = (
        "• Expanded Multi-Page Website: Complete service catalogs, portfolios, and customer reviews.\n"
        "• Secure Payment Gateway Integration: Collect online fees via UPI, QR, Credit Cards, Net Banking.\n"
        "• Luxury Physical Visiting Cards: Printed with high-grade matte & UV finish.\n"
        "• Interactive 3D Digital Business Card: Tap on any smartphone to save contact details & showcase work!"
    )
    p.font.size = Pt(10)
    p.font.color.rgb = TEXT_BODY

    # Right Bigli Image Card
    card_right = slide8.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE, Inches(8.1), Inches(1.7), Inches(4.4), Inches(5.2)
    )
    card_right.fill.solid()
    card_right.fill.fore_color.rgb = CARD_BG
    card_right.line.color.rgb = CARD_BORDER

    img_pro = os.path.join(IMAGES_DIR, "bigli_pro_pkg_1789839655537.jpg")
    if os.path.exists(img_pro):
        slide8.shapes.add_picture(img_pro, Inches(8.3), Inches(1.9), Inches(4.0), Inches(4.0))

    cap_box = slide8.shapes.add_textbox(Inches(8.2), Inches(6.0), Inches(4.2), Inches(0.8))
    tf = cap_box.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "Bigli's Pro Showcase: Tap-to-share NFC smart card + instant online customer payment collection."
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = CYAN_GLOW
    p.alignment = PP_ALIGN.CENTER

    slide8.notes_slide.notes_text_frame.text = (
        "TRAINER NOTES - PACKAGE 2:\n"
        "This is our most popular 'sweet spot' package! Business owners LOVE the digital visiting card feature. "
        "Demonstrate the tap-to-share feature on your own phone during the consultation. "
        "When they see that tapping a card against their client's phone instantly opens their website and saves contact details, "
        "it creates an irresistible 'wow' factor that justifies the ₹25,000 price on the spot."
    )

    # -------------------------------------------------------------
    # SLIDE 9: Package 3 (E-Commerce & WhatsApp AI Automation)
    # -------------------------------------------------------------
    slide9 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide9)
    add_header(
        slide9,
        "// Module 08: Product Portfolio (Tier 3)",
        "Package 3: E-Commerce & WhatsApp AI Automation Suite (₹50,000)",
        "The complete autopilot revenue system: online store coupled with 24/7 intelligent WhatsApp sales bot."
    )

    card_left = slide9.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.7), Inches(7.0), Inches(5.2)
    )
    card_left.fill.solid()
    card_left.fill.fore_color.rgb = CARD_BG
    card_left.line.color.rgb = CARD_BORDER

    tf = card_left.text_frame
    tf.word_wrap = True
    tf.margin_left = Inches(0.3)
    tf.margin_right = Inches(0.3)
    tf.margin_top = Inches(0.25)

    p = tf.paragraphs[0]
    p.text = "OFFICIAL PRICE: ₹50,000 (Enterprise Automation)"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = GREEN_ACCENT

    p = tf.add_paragraph()
    p.text = "Ideal For: D2C brands, restaurants, fashion boutiques, distributors, and multi-service healthcare."
    p.font.size = Pt(10)
    p.font.color.rgb = TEXT_MUTED
    p.space_after = Pt(8)

    # Script Box
    q_box = slide9.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.05), Inches(2.45), Inches(6.5), Inches(1.8)
    )
    q_box.fill.solid()
    q_box.fill.fore_color.rgb = QUOTE_BOX_BG
    q_box.line.color.rgb = QUOTE_BORDER
    q_box.line.width = Pt(1)

    tf_q = q_box.text_frame
    tf_q.word_wrap = True
    tf_q.margin_left = Inches(0.2)
    tf_q.margin_right = Inches(0.2)
    tf_q.margin_top = Inches(0.12)

    p = tf_q.paragraphs[0]
    p.text = (
        '"If you are looking to sell products online or fully automate your customer interactions, our E-Commerce & Smart Automation Package '
        'is designed for high revenue growth. You get a full multi-page E-Commerce storefront with online inventory management, '
        'coupled with an integrated WhatsApp Chatbot. The chatbot handles customer inquiries, sends updates, '
        'and drives automated sales 24/7 without requiring manual management."'
    )
    p.font.size = Pt(10)
    p.font.italic = True
    p.font.color.rgb = WHITE

    # Features
    p = tf.add_paragraph()
    p.text = "\nWHAT'S INCLUDED IN THE 24/7 REVENUE ENGINE:"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = CYAN_GLOW

    p = tf.add_paragraph()
    p.text = (
        "• Full Online Storefront: Product categories, image zoom, shopping cart, discounts & checkout.\n"
        "• Inventory & Order Management: Real-time stock alerts and merchant dashboard.\n"
        "• WhatsApp AI Automation Bot: Answers questions, captures customer details, and sends order receipts.\n"
        "• Zero Human Intervention: Your store makes sales even while the business owner is asleep."
    )
    p.font.size = Pt(10)
    p.font.color.rgb = TEXT_BODY

    # Right Bigli Image Card
    card_right = slide9.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE, Inches(8.1), Inches(1.7), Inches(4.4), Inches(5.2)
    )
    card_right.fill.solid()
    card_right.fill.fore_color.rgb = CARD_BG
    card_right.line.color.rgb = CARD_BORDER

    img_ecom = os.path.join(IMAGES_DIR, "bigli_ecom_ai_1789839680495.jpg")
    if os.path.exists(img_ecom):
        slide9.shapes.add_picture(img_ecom, Inches(8.3), Inches(1.9), Inches(4.0), Inches(4.0))

    cap_box = slide9.shapes.add_textbox(Inches(8.2), Inches(6.0), Inches(4.2), Inches(0.8))
    tf = cap_box.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "Bigli's Autopilot Store: Relax while the AI WhatsApp chatbot processes customer orders 24/7."
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = CYAN_GLOW
    p.alignment = PP_ALIGN.CENTER

    slide9.notes_slide.notes_text_frame.text = (
        "TRAINER NOTES - PACKAGE 3:\n"
        "This is our high-ticket premium suite (₹50,000). The pitch must focus on labor savings and 24/7 revenue. "
        "Point out that hiring a full-time sales assistant costs ₹15,000/month (₹1.8 Lakhs/year). "
        "Our WhatsApp chatbot never sleeps, never takes sick leave, and handles 50 customers simultaneously for a one-time setup fee!"
    )

    # -------------------------------------------------------------
    # SLIDE 10: Handling Objection 1 (The Cheap Website Trap)
    # -------------------------------------------------------------
    slide10 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide10)
    add_header(
        slide10,
        "// Module 09: Objection Mastery (Part 1)",
        "Overcoming Objection 1: 'Why ₹15,000+ When Others Are Cheaper?'",
        "The Digital Flyer Analogy: how to make cheap template competitors look like an expensive waste of money."
    )

    card_left = slide10.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.7), Inches(7.0), Inches(5.2)
    )
    card_left.fill.solid()
    card_left.fill.fore_color.rgb = CARD_BG
    card_left.line.color.rgb = CARD_BORDER

    tf = card_left.text_frame
    tf.word_wrap = True
    tf.margin_left = Inches(0.3)
    tf.margin_right = Inches(0.3)
    tf.margin_top = Inches(0.25)

    p = tf.paragraphs[0]
    p.text = 'CLIENT OBJECTION: "I found someone who will make a website for ₹2,000 or ₹5,000. Why pay ₹15,000+?"'
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = RED_ACCENT
    p.space_after = Pt(8)

    # Script Box
    q_box = slide10.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.05), Inches(2.35), Inches(6.5), Inches(2.25)
    )
    q_box.fill.solid()
    q_box.fill.fore_color.rgb = QUOTE_BOX_BG
    q_box.line.color.rgb = QUOTE_BORDER
    q_box.line.width = Pt(1)

    tf_q = q_box.text_frame
    tf_q.word_wrap = True
    tf_q.margin_left = Inches(0.2)
    tf_q.margin_right = Inches(0.2)
    tf_q.margin_top = Inches(0.12)

    p = tf_q.paragraphs[0]
    p.text = (
        '"A cheap template website acts like a digital flyer thrown on an empty sidewalk—no one sees it, '
        'it crashes on mobile phones, and it rarely converts visitors into buyers.\n\n'
        'At VTKRO, we don\'t just build static pages; we build conversion machines. Our packages include high-speed optimized code, '
        'flawless mobile responsiveness, fast cloud hosting, and business integrations like payment gateways and AI automation '
        'to generate actual leads and paying customers for your business."'
    )
    p.font.size = Pt(10)
    p.font.italic = True
    p.font.color.rgb = WHITE

    # Tactical Breakdown
    p = tf.add_paragraph()
    p.text = "\nTHE CORE COMPARISON TO DRILL INTO THE CLIENT:"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = GOLD

    p = tf.add_paragraph()
    p.text = (
        "• Cheap ₹3,000 Sites: Slow, broken formatting, zero SEO, hidden recurring server fees, no lead capture.\n"
        "• VTKRO Conversion Machines: Ultra-fast load (<2s), WhatsApp 1-tap ordering, lead database, guaranteed ROI."
    )
    p.font.size = Pt(10)
    p.font.color.rgb = TEXT_BODY

    # Right Bigli Image Card
    card_right = slide10.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE, Inches(8.1), Inches(1.7), Inches(4.4), Inches(5.2)
    )
    card_right.fill.solid()
    card_right.fill.fore_color.rgb = CARD_BG
    card_right.line.color.rgb = CARD_BORDER

    img_cheap = os.path.join(IMAGES_DIR, "bigli_cheap_vs_pro_1789840140905.jpg")
    if os.path.exists(img_cheap):
        slide10.shapes.add_picture(img_cheap, Inches(8.3), Inches(1.9), Inches(4.0), Inches(4.0))

    cap_box = slide10.shapes.add_textbox(Inches(8.2), Inches(6.0), Inches(4.2), Inches(0.8))
    tf = cap_box.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "Bigli's Conversion Law: Don't buy a digital flyer; invest in a high-converting revenue rocket!"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = CYAN_GLOW
    p.alignment = PP_ALIGN.CENTER

    slide10.notes_slide.notes_text_frame.text = (
        "TRAINER NOTES - PRICE OBJECTION:\n"
        "Never get defensive when clients mention cheap alternatives. Agree with them first! "
        "Say: 'You are completely right, there are ₹2,000 templates everywhere.' "
        "Then hit them with the contrast: 'The real question is: Do you want an online flyer that costs you money, "
        "or a digital asset that pays for itself in new client orders within 30 days?'"
    )

    # -------------------------------------------------------------
    # SLIDE 11: Handling Objection 2 ("I Already Have a Website")
    # -------------------------------------------------------------
    slide11 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide11)
    add_header(
        slide11,
        "// Module 10: Objection Mastery (Part 2)",
        "Overcoming Objection 2: 'I Already Have a Website!'",
        "How to validate their existing setup and expose the gap between a passive brochure and an active sales engine."
    )

    card_left = slide11.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.7), Inches(7.0), Inches(5.2)
    )
    card_left.fill.solid()
    card_left.fill.fore_color.rgb = CARD_BG
    card_left.line.color.rgb = CARD_BORDER

    tf = card_left.text_frame
    tf.word_wrap = True
    tf.margin_left = Inches(0.3)
    tf.margin_right = Inches(0.3)
    tf.margin_top = Inches(0.25)

    p = tf.paragraphs[0]
    p.text = 'CLIENT OBJECTION: "We already had a website made 2 years ago, so we\'re good."'
    p.font.size = Pt(11.5)
    p.font.bold = True
    p.font.color.rgb = RED_ACCENT
    p.space_after = Pt(8)

    # Script Box
    q_box = slide11.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.05), Inches(2.35), Inches(6.5), Inches(2.25)
    )
    q_box.fill.solid()
    q_box.fill.fore_color.rgb = QUOTE_BOX_BG
    q_box.line.color.rgb = QUOTE_BORDER
    q_box.line.width = Pt(1)

    tf_q = q_box.text_frame
    tf_q.word_wrap = True
    tf_q.margin_left = Inches(0.2)
    tf_q.margin_right = Inches(0.2)
    tf_q.margin_top = Inches(0.12)

    p = tf_q.paragraphs[0]
    p.text = (
        '"That\'s great! Having a site proves you understand the importance of being online.\n\n'
        'Quick question: Is your current site equipped with an automated WhatsApp chatbot to capture inquiries instantly, '
        'or can customers pay you directly in one click?\n\n'
        'We don\'t ask you to discard what you have—we help upgrade your existing online setup into a 24/7 automated sales system."'
    )
    p.font.size = Pt(10.5)
    p.font.italic = True
    p.font.color.rgb = WHITE

    # Tactical Breakdown
    p = tf.add_paragraph()
    p.text = "\nTHE 3-STEP PSYCHOLOGICAL PIVOT:"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = GOLD

    p = tf.add_paragraph()
    p.text = (
        "1. Praise & Validate: Congratulate them on already having a web presence.\n"
        "2. The Diagnosis Question: Expose modern missing features (Instant WhatsApp bot, direct UPI payments).\n"
        "3. Position as an Upgrade: Frame VTKRO as modernizing their engine rather than tearing it down."
    )
    p.font.size = Pt(10)
    p.font.color.rgb = TEXT_BODY

    # Right Bigli Image Card
    card_right = slide11.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE, Inches(8.1), Inches(1.7), Inches(4.4), Inches(5.2)
    )
    card_right.fill.solid()
    card_right.fill.fore_color.rgb = CARD_BG
    card_right.line.color.rgb = CARD_BORDER

    img_upgrade = os.path.join(IMAGES_DIR, "bigli_upgrade_site_1789840163493.jpg")
    if os.path.exists(img_upgrade):
        slide11.shapes.add_picture(img_upgrade, Inches(8.3), Inches(1.9), Inches(4.0), Inches(4.0))

    cap_box = slide11.shapes.add_textbox(Inches(8.2), Inches(6.0), Inches(4.2), Inches(0.8))
    tf = cap_box.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "Bigli's Upgrade Blueprint: Turn sleepy inactive websites into modern automated sales powerhouses."
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = CYAN_GLOW
    p.alignment = PP_ALIGN.CENTER

    slide11.notes_slide.notes_text_frame.text = (
        "TRAINER NOTES - EXISTING WEBSITE OBJECTION:\n"
        "Most businesses built a website 4 years ago on outdated WordPress that nobody updates. "
        "It doesn't take online payments, it has no WhatsApp lead bot, and it looks broken on iPhone/Android. "
        "Show them how VTKRO upgrades their stagnant presence into an active revenue channel."
    )

    # -------------------------------------------------------------
    # SLIDE 12: The Closing Strategy (Double Choice & Demo Slot)
    # -------------------------------------------------------------
    slide12 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide12)
    add_header(
        slide12,
        "// Module 11: Closing Formula",
        "The Power Close: The Double-Alternative & Demo Booking",
        "How to eliminate rejection by replacing 'Yes/No' questions with structured choices."
    )

    card_left = slide12.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.7), Inches(7.0), Inches(5.2)
    )
    card_left.fill.solid()
    card_left.fill.fore_color.rgb = CARD_BG
    card_left.line.color.rgb = CARD_BORDER

    tf = card_left.text_frame
    tf.word_wrap = True
    tf.margin_left = Inches(0.3)
    tf.margin_right = Inches(0.3)
    tf.margin_top = Inches(0.25)

    p = tf.paragraphs[0]
    p.text = "THE OFFICIAL HIGH-CONVERTING CLOSING SCRIPT"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = CYAN_GLOW

    # Script Box
    q_box = slide12.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.05), Inches(2.15), Inches(6.5), Inches(2.3)
    )
    q_box.fill.solid()
    q_box.fill.fore_color.rgb = QUOTE_BOX_BG
    q_box.line.color.rgb = QUOTE_BORDER
    q_box.line.width = Pt(1)

    tf_q = q_box.text_frame
    tf_q.word_wrap = True
    tf_q.margin_left = Inches(0.2)
    tf_q.margin_right = Inches(0.2)
    tf_q.margin_top = Inches(0.12)

    p = tf_q.paragraphs[0]
    p.text = (
        '"Based on your current operations at [Client\'s Business Name], would you prefer starting with our '
        '₹15,000 Standard Site, upgrading to the ₹25,000 Payment & Branding Suite, or leveraging the ₹50,000 E-Commerce & WhatsApp Chatbot Setup?\n\n'
        'I can reserve a slot for our senior technical strategist to run a quick 10-minute demo for you this afternoon. '
        'Would 3:00 PM or 5:00 PM work better?"'
    )
    p.font.size = Pt(10.5)
    p.font.italic = True
    p.font.color.rgb = WHITE

    # Closing Principles
    p = tf.add_paragraph()
    p.text = "\nTWO FATAL CLOSING MISTAKES & THE SOLUTION:"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = GOLD

    p = tf.add_paragraph()
    p.text = (
        "• NEVER ASK: 'Do you want to buy?' or 'What do you think?' (Invites a fast 'No' or 'Let me think about it').\n"
        "• ALWAYS USE THE DOUBLE-ALTERNATIVE: When you offer '3:00 PM or 5:00 PM?', their brain evaluates "
        "which time fits their schedule, rather than deciding whether to say yes or no!"
    )
    p.font.size = Pt(10)
    p.font.color.rgb = TEXT_BODY

    # Right Bigli Image Card
    card_right = slide12.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE, Inches(8.1), Inches(1.7), Inches(4.4), Inches(5.2)
    )
    card_right.fill.solid()
    card_right.fill.fore_color.rgb = CARD_BG
    card_right.line.color.rgb = CARD_BORDER

    img_close = os.path.join(IMAGES_DIR, "bigli_demo_close_1789840447287.jpg")
    if os.path.exists(img_close):
        slide12.shapes.add_picture(img_close, Inches(8.3), Inches(1.9), Inches(4.0), Inches(4.0))

    cap_box = slide12.shapes.add_textbox(Inches(8.2), Inches(6.0), Inches(4.2), Inches(0.8))
    tf = cap_box.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "Bigli's Demo Close: Book the slot with '3:00 PM or 5:00 PM' and seal the deal smoothly."
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = CYAN_GLOW
    p.alignment = PP_ALIGN.CENTER

    slide12.notes_slide.notes_text_frame.text = (
        "TRAINER NOTES - CLOSING TECHNIQUE:\n"
        "Notice the wording: You are NOT trying to close the entire ₹50,000 transaction over a 2-minute phone call. "
        "Your sole objective on the initial call is to CLOSE THE 10-MINUTE DEMO! "
        "When our senior technical strategist gets on that 10-minute demo with the client, the closing rate is over 60%."
    )

    # -------------------------------------------------------------
    # SLIDE 13: Agent Success Blueprint (The Champion Routine)
    # -------------------------------------------------------------
    slide13 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide13)
    add_header(
        slide13,
        "// Module 12: Agent Blueprint & Commission Math",
        "The Champion Agent Daily Routine & Earning Blueprint",
        "Consistency + Strategy = Elite Earnings. The predictable math behind making ₹50,000 to ₹1,50,000/month."
    )

    card_left = slide13.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.7), Inches(7.0), Inches(5.2)
    )
    card_left.fill.solid()
    card_left.fill.fore_color.rgb = CARD_BG
    card_left.line.color.rgb = CARD_BORDER

    tf = card_left.text_frame
    tf.word_wrap = True
    tf.margin_left = Inches(0.3)
    tf.margin_right = Inches(0.3)
    tf.margin_top = Inches(0.25)

    p = tf.paragraphs[0]
    p.text = "THE PREDICTABLE MATH OF HIGH COMMISSIONS"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = GREEN_ACCENT

    p = tf.add_paragraph()
    p.text = (
        "• 10 Phone Briefings Daily = 50 Briefings / Week\n"
        "• 2 Confirmed 10-Minute Demos Booked Daily = 10 Demos / Week\n"
        "• 2 to 3 Deals Closed Weekly = 8 to 12 Deals / Month\n"
        "• Estimated Monthly Agent Commissions: ₹40,000 – ₹1,20,000+ !"
    )
    p.font.size = Pt(10.5)
    p.font.color.rgb = TEXT_BODY
    p.space_after = Pt(10)

    p = tf.add_paragraph()
    p.text = "AGENT CONSULTANT SANJAI KUMAR'S 4 GOLDEN RULES:"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = GOLD

    p = tf.add_paragraph()
    p.text = (
        "1. Always Call First: Brief by phone and set a time. Never barge in unannounced.\n"
        "2. Segment by Scale: Sell Quality to big businesses; sell Cost-Efficiency to small shops.\n"
        "3. Protect Pricing: Use the Corporate Shield or Intern Challenge with relatives.\n"
        "4. Close on the Demo: Use the 3 PM vs 5 PM alternative choice to lock in the demonstration."
    )
    p.font.size = Pt(10)
    p.font.color.rgb = WHITE
    p.space_after = Pt(10)

    p = tf.add_paragraph()
    p.text = "WE ARE HERE TO WIN TOGETHER. WELCOME TO THE VTKRO SUCCESS ENGINE!"
    p.font.size = Pt(10.5)
    p.font.bold = True
    p.font.color.rgb = CYAN_GLOW

    # Right Bigli Image Card
    card_right = slide13.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE, Inches(8.1), Inches(1.7), Inches(4.4), Inches(5.2)
    )
    card_right.fill.solid()
    card_right.fill.fore_color.rgb = CARD_BG
    card_right.line.color.rgb = CARD_BORDER

    img_trophy = os.path.join(IMAGES_DIR, "bigli_trophy_1789840487945.jpg")
    if os.path.exists(img_trophy):
        slide13.shapes.add_picture(img_trophy, Inches(8.3), Inches(1.9), Inches(4.0), Inches(4.0))

    cap_box = slide13.shapes.add_textbox(Inches(8.2), Inches(6.0), Inches(4.2), Inches(0.8))
    tf = cap_box.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "Bigli the Champion: Follow the system, maintain daily consistency, and take the #1 podium!"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = CYAN_GLOW
    p.alignment = PP_ALIGN.CENTER

    slide13.notes_slide.notes_text_frame.text = (
        "TRAINER NOTES - GRADUATION & WRAP-UP:\n"
        "End with total empowerment. Remind them: 'Sales is not luck; it is a numbers game guided by a proven script.' "
        "If an agent makes 10 calls every morning before lunch, they will never have to worry about money again. "
        "Tell them to save this presentation on their phone, review it every morning, and get on the phones today!"
    )

    output_path = os.path.abspath("VTKRO_Agent_Sales_Masterclass.pptx")
    prs.save(output_path)
    print(f"Presentation successfully created at: {output_path}")

if __name__ == "__main__":
    create_presentation()
