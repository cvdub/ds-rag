# Plan: Converting Draw Steel Heroes to Formal Game Rules Specification

## Executive Summary

This document outlines a comprehensive plan for converting the "Draw Steel Heroes - Unlinked.md" document (1.9MB, ~27,760 lines) into a formal game rules specification. The specification will focus purely on game mechanics and rules without any coding-related design considerations.

## Source Document Analysis

### Document Structure
The Draw Steel Heroes document contains 17 main chapters with approximately 2,400 subsections:

1. **Introduction** - Game overview and design philosophy
2. **The Basics** - Core mechanics (dice, characteristics, power rolls)
3. **Making a Hero** - Character creation process
4. **Ancestries** - Player species/races
5. **Background** - Character culture and career
6. **Classes** - Character classes and abilities
7. **Kits** - Equipment and starting gear systems
8. **Perks** - Additional character benefits
9. **Complications** - Character background complications
10. **Tests** - Skill check and test resolution system
11. **Combat** - Tactical combat rules
12. **Negotiation** - Social encounter mechanics
13. **Downtime Projects** - Between-adventure activities
14. **Rewards** - Treasure, experience, and advancement
15. **Gods and Religion** - Divine mechanics
16. **For the Director** - Game master guidance
17. **Draw Steel Creator License** - Licensing information

### Key Game Systems Identified

**Core Mechanics:**
- 2d10 dice system with tier-based outcomes (Tier 1, 2, 3)
- Five characteristics: Might, Agility, Reason, Intuition, Presence
- Power rolls with edges/banes system
- Hero tokens as meta-currency
- Heroic Resources (class-specific resources)

**Character Systems:**
- Ancestry, Culture, Career background system
- Class-based progression (Censor, Conduit, etc.)
- Kit system for equipment loadouts
- Skill-based tests system
- Complication system for narrative depth

**Combat Systems:**
- Grid-based tactical combat
- Turn structure with maneuvers and main actions
- Stamina and Recovery system
- Condition system (bleeding, dazed, frightened, etc.)
- Area effects (aura, burst, cube, line, wall)
- Movement modes (burrow, climb, fly, swim)

**Non-Combat Systems:**
- Negotiation encounter structure
- Downtime project system
- Victory and experience tracking
- Respite (rest) mechanics

## Specification Goals

### Primary Objectives
1. **Clarity and Precision**: Define all game rules with unambiguous language
2. **Completeness**: Cover all mechanical systems comprehensively
3. **Organization**: Structure information logically for easy reference
4. **Consistency**: Use standardized terminology throughout
5. **Accessibility**: Make rules easy to understand and apply

### Scope
- **Include**: All game mechanics, resolution systems, character options, combat rules, and numerical values
- **Exclude**: Setting lore, flavor text, design philosophy, example play scenarios, and licensing
- **Focus**: Pure rules specification without implementation details

## Proposed Specification Structure

### 1. Core Rules Specification

#### 1.1 Fundamental Mechanics
- Dice notation and rolling procedures
- Characteristic system definition
- Power roll resolution algorithm
- Edge and bane mechanics
- Bonus and penalty application rules
- Automatic tier outcomes

#### 1.2 Resource Systems
- Hero tokens (earning and spending)
- Heroic Resources (class-specific)
- Stamina system
- Recovery system
- Victory tracking

#### 1.3 Universal Game Concepts
- Creature definitions and classifications
- Object interaction rules
- Distance and measurement
- Time units (rounds, turns, encounters)
- Supernatural vs mundane effects

### 2. Character Specification

#### 2.1 Character Creation Rules
- Step-by-step creation algorithm
- Characteristic generation/assignment
- Starting resources calculation
- Equipment acquisition rules

#### 2.2 Character Components
- **Ancestry Rules**
  - Mechanical benefits by ancestry
  - Ancestry-specific abilities
  - Size and movement rules

- **Background Rules**
  - Culture mechanical effects
  - Career mechanical effects
  - Skill selections

- **Class Rules**
  - Class features by level
  - Ability acquisition rules
  - Heroic Resource mechanics per class
  - Subclass/archetype rules

- **Kit Rules**
  - Kit composition
  - Starting equipment by kit
  - Kit-specific abilities

- **Perk Rules**
  - Perk selection mechanics
  - Perk effects and restrictions

- **Complication Rules** (Optional)
  - Complication selection
  - Mechanical benefits and drawbacks

#### 2.3 Character Advancement
- Experience point rules
- Level-up procedures
- Ability score increases
- Feature acquisition by level
- Alternative advancement systems

### 3. Action Resolution Specification

#### 3.1 Test System
- Test resolution procedure
- Skill application rules
- Difficulty tier assignments
- Success and failure outcomes
- Consequence mechanics
- Edge/bane application in tests

#### 3.2 Skill System
- Complete skill list
- Skill descriptions and applications
- Skill-characteristic flexibility
- Skill specializations

### 4. Combat System Specification

#### 4.1 Combat Structure
- Initiative and turn order
- Combat round definition
- Turn phases and action economy
- End of turn procedures

#### 4.2 Action Types
- **Maneuvers**
  - Standard maneuver list
  - Maneuver resolution rules
  - Opportunity costs

- **Main Actions**
  - Action types and restrictions
  - Free strike mechanics
  - Charge action rules

- **Triggered Actions**
  - Trigger conditions
  - Timing and resolution

- **Movement Actions**
  - Advance move rules
  - Special movement types

#### 4.3 Abilities
- Ability structure definition
- Ability keywords and their effects
- Ability roll resolution
- Damage calculation
- Effect application

#### 4.4 Targeting and Range
- Line of effect rules
- Range measurement
- Area of effect types (aura, burst, cube, line, wall)
- Target selection restrictions

#### 4.5 Positioning and Movement
- Grid-based positioning
- Movement rules by terrain
- Forced movement rules
- Movement mode definitions (climb, fly, burrow, swim)
- Difficult terrain rules

#### 4.6 Damage and Healing
- Damage type system
- Damage calculation procedures
- Resistance and immunity rules
- Healing mechanics
- Temporary stamina rules
- Death and dying rules

#### 4.7 Conditions
- Complete condition list with mechanical effects:
  - Bleeding
  - Dazed
  - Frightened
  - Grabbed
  - Prone
  - Restrained
  - Slowed
  - Taunted
  - Weakened
- Condition application and removal
- Condition interaction rules

#### 4.8 Combat Modifiers
- Cover rules and effects
- Concealment rules and effects
- Advantage/disadvantage situations
- Environmental effects

### 5. Negotiation System Specification

#### 5.1 Negotiation Structure
- Negotiation encounter setup
- Participant roles
- Round structure

#### 5.2 Negotiation Mechanics
- Argument system
- Interest and motivation mechanics
- Success and failure conditions
- Consequence application

#### 5.3 Negotiation Actions
- Available actions in negotiation
- Resolution procedures
- Social condition effects

### 6. Downtime System Specification

#### 6.1 Respite Rules
- Respite duration and requirements
- Resource recovery during respite
- Activity restrictions

#### 6.2 Project System
- Project types and definitions
- Project roll mechanics
- Breakthrough rules
- Success and failure outcomes
- Crafting project rules
- Research project rules
- Other project categories

### 7. Rewards and Progression Specification

#### 7.1 Experience System
- XP award guidelines
- Victory-based XP
- Milestone XP alternatives
- Level progression table

#### 7.2 Treasure System
- Treasure types (consumable, artifact, etc.)
- Treasure distribution rules
- Treasure effects and mechanics
- Magic item rules

#### 7.3 Followers and Holdings
- Follower types and rules
- Follower action mechanics
- Holdings system (if applicable)

### 8. Reference Tables and Appendices

#### 8.1 Quick Reference Tables
- Characteristic score effects
- Power roll tier outcomes
- Condition quick reference
- Action economy summary
- Movement costs table
- Standard difficulty tiers

#### 8.2 Ability Compendium
- All class abilities organized by class and level
- Standardized ability format:
  - Name
  - Type (maneuver/main action/triggered action)
  - Keywords
  - Requirements
  - Target specifications
  - Effect by tier
  - Special rules

#### 8.3 Equipment Compendium
- Complete equipment list
- Weapon statistics
- Armor statistics
- Gear descriptions
- Cost and availability

#### 8.4 Glossary
- Alphabetical listing of all game terms
- Cross-references
- Standardized definitions

## Conversion Methodology

### Phase 1: Extraction and Categorization
1. Parse the source document by section
2. Identify all mechanical rules vs flavor text
3. Categorize rules by system (core, combat, character, etc.)
4. Extract all tables, statistics, and numerical values
5. Create a comprehensive list of game terms

### Phase 2: Standardization
1. Define standardized terminology
2. Create consistent formatting for similar rule types
3. Establish naming conventions
4. Develop standard templates for recurring elements (abilities, items, etc.)
5. Identify and resolve terminology conflicts

### Phase 3: Specification Writing
1. Write each section in formal specification language
2. Use consistent structure:
   - Rule statement
   - Procedure/algorithm
   - Exceptions and edge cases
   - Cross-references
3. Include mathematical formulas where applicable
4. Add clarifying notes for complex interactions

### Phase 4: Organization and Cross-Referencing
1. Create logical hierarchy
2. Add internal cross-references
3. Build index and glossary
4. Create quick-reference sections
5. Develop table of contents with detailed page references

### Phase 5: Validation and Review
1. Check for completeness against source
2. Verify internal consistency
3. Ensure no ambiguous language
4. Validate all cross-references
5. Test rule clarity with edge cases

## Specification Format Guidelines

### Language Standards
- Use imperative mood for procedures ("Roll 2d10", not "You roll 2d10")
- Use present tense for rules ("A creature gains", not "A creature will gain")
- Avoid ambiguous terms (use "must" for requirements, "may" for options)
- Define acronyms on first use
- Use consistent numerical formatting

### Structural Standards
- Hierarchical numbering system (1.0, 1.1, 1.1.1)
- Consistent heading levels
- Boxed text for important rules
- Tables for related statistics
- Bullet points for lists
- Examples only when clarifying complex rules

### Documentation Standards
- Each rule should be independently understandable with cross-references
- Technical precision over readability (but maintain both when possible)
- Include "see section X.X" for related rules
- Use consistent templates for similar content types
- Maintain traceability to source document sections

## Key Considerations

### Handling Ambiguities
- When source rules are ambiguous, document the ambiguity
- Provide logical interpretation based on game system patterns
- Note areas requiring playtesting or clarification
- Cross-reference with related rules for consistency

### Completeness Checks
- Ensure every character option has complete mechanical definition
- Verify all conditions have clear effects
- Confirm all abilities have full stat blocks
- Validate all systems have resolution procedures
- Check for orphaned references

### Maintaining Neutrality
- Avoid game balance commentary
- Don't suggest house rules or variants
- Present rules as they exist in source
- Don't prioritize one playstyle over another
- Focus on "what" and "how", not "why" or "should"

## Deliverables

### Primary Deliverable
**Formal Game Rules Specification Document** containing:
- Complete rule specifications organized by system
- Comprehensive reference tables
- Full ability and equipment compendiums
- Detailed glossary and index
- Cross-reference system

### Format Options
1. **Single comprehensive document** (markdown format)
2. **Modular specification** (separate documents by major system)
3. **Hierarchical structure** (core rules + system supplements)

Recommended: Start with modular approach for easier maintenance and reference, with option to compile into single document.

## Success Criteria

The specification will be considered complete and successful when:

1. **Coverage**: All mechanical systems from source are documented
2. **Clarity**: Rules are unambiguous and precisely stated
3. **Accessibility**: Information is easy to find and reference
4. **Consistency**: Terminology and formatting are standardized
5. **Independence**: Rules can be understood without source document
6. **Practicality**: Specification can be used for actual play
7. **Neutrality**: No coding or implementation bias included

## Next Steps

### Immediate Actions
1. Obtain complete source document access
2. Set up document parsing tools/workflow
3. Create specification template structure
4. Begin extraction of core mechanics
5. Start building glossary and term database

### Prioritization
**Priority 1**: Core mechanics and character creation (most frequently referenced)
**Priority 2**: Combat system (most complex and detailed)
**Priority 3**: Tests, negotiation, and downtime (secondary systems)
**Priority 4**: Reference tables and compendiums (supporting material)
**Priority 5**: Advanced rules and optional systems (edge cases)

## Maintenance Considerations

Since Draw Steel may receive updates or errata:
- Use version numbers for specification
- Maintain changelog
- Track source document version/date
- Design modular structure for easy updates
- Document assumptions made during conversion

## Estimated Scope

Based on source analysis:
- **Core Rules**: ~50-75 pages of specification
- **Character Systems**: ~100-150 pages
- **Combat System**: ~75-100 pages
- **Other Systems**: ~50-75 pages
- **Reference Material**: ~100-150 pages
- **Total Estimated**: 375-550 pages of formal specification

This accounts for the need to expand abbreviated rules into full specifications and the addition of comprehensive tables and cross-references.

## Conclusion

This plan provides a structured approach to converting the Draw Steel Heroes document into a formal game rules specification. The specification will serve as a precise, comprehensive, and accessible reference for the game's mechanical systems, suitable for players, game masters, and anyone needing to understand the game's rules in detail without any implementation or coding considerations.
